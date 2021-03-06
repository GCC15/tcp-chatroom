"""Main controller of the SCRP server"""

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

import sys

import daemon


def main():
    if len(sys.argv) != 2:
        _print_usage_and_exit()
    action = sys.argv[1]
    if action == 'start':
        daemon.start()
    elif action == 'stop':
        daemon.stop()
    elif action == 'status':
        daemon.status()
    else:
        _print_usage_and_exit()


def _print_usage_and_exit():
    print('Usage: <python> {} start|stop|status'.format(sys.argv[0]))
    sys.exit(1)


if __name__ == '__main__':
    main()
