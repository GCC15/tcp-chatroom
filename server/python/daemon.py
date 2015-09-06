"""SCRP server daemon"""

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

import socket
import scrp_server
import os
import socket
import subprocess
import sys

import env

env.make_dirs(env.get_var_dir())
_lock_file_path = os.path.join(env.get_var_dir(), env.get_lock_file())


def start():
    """Start daemon process"""
    if os.path.isfile(_lock_file_path):
        print('Error: Server already started')
    else:
        args = sys.executable, __file__
        pid = _start_daemon(args).pid
        print('Server started with PID {}'.format(pid))
        with open(_lock_file_path, 'w') as f:
            f.write(str(pid))


def stop():
    """Stop daemon process"""
    if os.path.isfile(_lock_file_path):
        s = socket.socket()
        # TODO
        os.remove(_lock_file_path)
        print('Server stopped')
    else:
        print('Error: Server is not running')


def status():
    """Check if daemon is running"""
    if os.path.isfile(_lock_file_path):
        with open(_lock_file_path) as f:
            pid = f.read()
        print('Server is running with PID {}'.format(pid))
    else:
        print('Server is not running')


def _start_daemon(args: tuple) -> subprocess.Popen:
    if env.IS_WIN32:
        return subprocess.Popen(args, creationflags=env.WIN32_DETACHED_PROCESS)
    else:
        return subprocess.Popen(args)


def main():
    while True:
        pass
        # TODO
        # server = scrp_server.Server()


if __name__ == '__main__':
    main()
