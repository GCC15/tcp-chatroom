"""
Low-level abstraction of the database
A queue is used to ensure that DB operations are performed in the same thread.
"""

import threading
import queue
import os
import sqlite3

import config as cfg


class _ManagerThread(threading.Thread):
    def __init__(self):
        super().__init__(name='DBManagerThread', daemon=True)
        var_dir = cfg.get('var_dir')
        cfg.make_dirs(var_dir)
        db_file = cfg.get('db_file')
        self._db_file_path = os.path.join(var_dir, db_file)
        # Store the result of the last task
        self._result = None
        # Task queue
        self._q = queue.Queue()

    def run(self):
        conn = sqlite3.connect(self._db_file_path)
        while True:
            func, event = self._q.get()
            self._result = func(conn.cursor())
            conn.commit()
            self._q.task_done()
            event.set()

    def execute(self, func):
        event = threading.Event()
        self._q.put((func, event))
        event.wait()
        return self._result


_mt = _ManagerThread()
_mt.start()


def execute(func):
    """func receives one Cursor argument"""
    return _mt.execute(func)


def main(i):
    """For testing"""
    print('{} WAITING IN {}'.format(i, threading.current_thread().name))

    def task(c):
        print('{} RUNNING IN {}'.format(i, threading.current_thread().name))
        time.sleep(random.random())
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
