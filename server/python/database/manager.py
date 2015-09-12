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

_var_dir = env.get_var_dir()
env.make_dirs(_var_dir)
_db_file = env.get_db_file()
_db_file_path = os.path.join(_var_dir, _db_file)

# Task and result
_func = None
_result = None

# Synchronization
_exec_lock = threading.Lock()
_task_event = threading.Event()
_result_event = threading.Event()
_shutting_down = False


def manage():
    global _result
    conn = sqlite3.connect(_db_file_path)
    while True:
        _task_event.wait()
        # Block
        _task_event.clear()
        if _shutting_down:
            break
        # noinspection PyCallingNonCallable
        _result = _func(conn.cursor)
        conn.commit()
        _result_event.set()


_manager_thread = threading.Thread(target=manage, name="DBManagerThread")
_manager_thread.start()


def execute(func):
    """
    Perform some DB operations.
    func receives a cursor factory function () -> Cursor as the argument
    """
    global _func
    with _exec_lock:
        # Only one thread can enter the block at the same time
        if _shutting_down:
            return
        _func = func
        _task_event.set()
        _result_event.wait()
        # Block
        _result_event.clear()
        return _result


def shutdown():
    """
    Shutdown the DB manager thread.
    Blocks until the manager thread stops safely.
    """
    global _shutting_down
    with _exec_lock:
        _shutting_down = True
        _task_event.set()
        _manager_thread.join()


def main():
    """For testing"""

    def task(cursor_factory):
        c = cursor_factory()
        c.execute('SELECT -?', [42])
        return c.fetchone()[0]

    print(execute(task))
    shutdown()


if __name__ == '__main__':
    main()
