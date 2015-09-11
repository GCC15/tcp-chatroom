"""Environment variables and constants"""

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

import os
import sys

import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def make_dirs(directory: str):
    """Create a directory and its parents, if necessary"""
    if not os.path.exists(directory):
        os.makedirs(directory)


IS_WIN32 = (sys.platform == 'win32')
WIN32_DETACHED_PROCESS = 0x00000008

_config_dict = json.load(open('config.json'))


def _get(key: str):
    """Get entry from config.json"""
    return _config_dict[key]


def get_server_nickname() -> str:
    return _get('server_nickname')


def get_server_version() -> str:
    return _get('server_version')


def get_server_description() -> str:
    return _get('server_description')


def get_server_protocol_version() -> str:
    return _get('server_protocol_version')


def get_var_dir() -> str:
    return _get('var_dir')


def get_log_file() -> str:
    return _get('log_file')


def get_db_file() -> str:
    return _get('db_file')


def get_lock_file() -> str:
    return _get('lock_file')


def get_server_port() -> int:
    return _get('server_port')


def get_control_port() -> int:
    return _get('control_port')


def get_tcp_listen_backlog() -> int:
    return _get('tcp_listen_backlog')


def get_salt_length() -> int:
    return _get('salt_length')
