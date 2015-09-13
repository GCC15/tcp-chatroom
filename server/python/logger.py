"""Basic thread-safe logging"""

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

from enum import Enum
import os
import threading
import time

import env

_var_dir = env.get_var_dir()
env.make_dirs(_var_dir)
_log_file = env.get_log_file()
_log_file_path = os.path.join(_var_dir, _log_file)
_f = None

_log_lock = threading.Lock()


def _open_log_file():
    global _f
    if _f is None or _f.closed:
        _f = open(_log_file_path, 'a')
    return _f


def _close_log_file():
    global _f
    if _f is not None and not _f.closed:
        _f.close()


class Level(Enum):
    debug = 'Debug'
    info = 'Info'
    warning = 'Warning'
    error = 'Error'


def _log(level: Level, message: str):
    with _log_lock:
        s = '[{}] {}({}): {}'.format(
            time.ctime(),
            level.value,
            threading.current_thread().name,
            message
        )
        print(s)
        f = _open_log_file()
        f.write(s + '\n')
        f.flush()


def d(message: str):
    """Debug"""
    _log(Level.debug, message)


def i(message: str):
    """Info"""
    _log(Level.info, message)


def w(message: str):
    """Warning"""
    _log(Level.warning, message)


def e(message: str):
    """Error"""
    _log(Level.error, message)


def clear():
    """Clear and remove the log file"""
    with _log_lock:
        _close_log_file()
        if os.path.isfile(_log_file_path):
            os.remove(_log_file_path)


def main():
    clear()


if __name__ == '__main__':
    main()
