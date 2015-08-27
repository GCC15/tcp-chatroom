"""Configurations and generic file system operations"""

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

import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def _load_config_dict():
    return json.load(open('config.json'))


_config_dict = _load_config_dict()


def get(key):
    return _config_dict[key]


def make_dirs(directory):
    """Create a directory and its parents, if necessary"""
    if not os.path.exists(directory):
        os.makedirs(directory)
