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
        super().__init__(name='DBManagerThread')

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
        self.__shutting_down = False

    def run(self):
        conn = sqlite3.connect(self.__db_file_path)
        while True:
            self.__task_event.wait()
            # Block
            self.__task_event.clear()
            if self.__shutting_down:
                break
            # noinspection PyCallingNonCallable
            self.__result = self.__func(conn.cursor)
            conn.commit()
            self.__result_event.set()

    def execute(self, func):
        with self.__exec_lock:
            # Only one thread can enter the block at the same time
            if self.__shutting_down:
                return
            self.__func = func
            self.__task_event.set()
            self.__result_event.wait()
            # Block
            self.__result_event.clear()
            return self.__result

    def shutdown(self):
        with self.__exec_lock:
            self.__shutting_down = True
        self.__task_event.set()
        self.join()


_mt = _ManagerThread()
_mt.start()


def execute(func):
    """
    Perform some DB operations.
    func receives a cursor factory function () -> Cursor as the argument
    """
    return _mt.execute(func)


def shutdown():
    """
    Shutdown the DB manager thread.
    Blocks until the manager thread stops safely.
    """
    _mt.shutdown()


def main():
    """For testing"""
    def task(cursor_factory):
        c = cursor_factory()
        c.execute('SELECT ?', [42])
        return c.fetchone()[0]

    print(execute(task))
    shutdown()


if __name__ == '__main__':
    main()
