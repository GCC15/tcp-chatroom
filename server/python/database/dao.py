"""
High-level abstraction of the database
All functions are atomic.
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

from . import manager
from . import names
from . import helper
import model

DB_VERSION = 1  # Current DB version


def _check_db():
    """
    Upgrade the database if necessary.
    See CHANGELOG for changes made in each version.
    """
    existing_ver = helper.get_db_version()
    if existing_ver > DB_VERSION:
        raise ValueError(
            'DB version ({}) is older than the existing version ({})!'
                .format(DB_VERSION, existing_ver))
    elif existing_ver < DB_VERSION:
        input('DB needs to upgrade from version {} to {}. '
              'Press enter to continue...'
              .format(existing_ver, DB_VERSION))
        helper.upgrade_db(existing_ver, DB_VERSION)
        helper.set_db_version(DB_VERSION)
        print('DB upgrade complete!')


_check_db()


def add_user(user: model.User):
    def task(cursor_factory):
        c = cursor_factory()
        # TODO
        c.execute('INSERT INTO {} () VALUES ()'.format(names.TBL_USER))

    manager.execute(task)
