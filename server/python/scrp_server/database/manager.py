"""
Low-level abstraction of the database
Perform DB operations synchronously in the same thread.
"""

# Copyright (C) 2015 Zhang NS, Zifan Li, Zichao Li
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import threading
import os
import sqlite3

import env


class _ManagerThread(threading.Thread):
    def __init__(self):
        super().__init__(name='DBManagerThread', daemon=True)

        var_dir = env.get_var_dir()
        env.make_dirs(var_dir)
        db_file = env.get_db_file()
        self.__db_file_path = os.path.join(var_dir, db_file)

        self.__func = None
        self.__result = None

        # Synchronization
        self.__exec_lock = threading.Lock()
        self.__task_event = threading.Event()
        self.__result_event = threading.Event()

    def run(self):
        conn = sqlite3.connect(self.__db_file_path)
        while True:
            self.__task_event.wait()
            # Block
            self.__task_event.clear()
            # noinspection PyCallingNonCallable
            self.__result = self.__func(conn.cursor)
            conn.commit()
            self.__result_event.set()

    def execute(self, func):
        with self.__exec_lock:
            # Only one thread can enter the block at the same time
            self.__func = func
            self.__task_event.set()
            self.__result_event.wait()
            # Block
            self.__result_event.clear()
            return self.__result


_mt = _ManagerThread()
_mt.start()


def execute(func):
    """func receives a cursor factory function () -> Cursor as the argument"""
    return _mt.execute(func)


def main(i):
    """For testing"""
    print('{} WAITING IN {}'.format(i, threading.current_thread().name))

    def task(cursor_factory):
        print('{} RUNNING IN {}'.format(i, threading.current_thread().name))
        time.sleep(random.random())
        c = cursor_factory()
        c.execute('SELECT -{}'.format(i))
        ret = c.fetchall()
        print('{} RETURNING'.format(i))
        return ret

    print('{} RESULT {}'.format(i, execute(task)))


if __name__ == '__main__':
    import time
    import random

    for _i in range(5):
        threading.Thread(target=main, args=(_i + 1,)).start()
