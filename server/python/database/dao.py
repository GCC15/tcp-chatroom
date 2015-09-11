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

import random
import string
import hashlib

import env
from . import manager
from . import helper
from .names import *
from model.data import *

DB_VERSION = 1  # Current DB version


def _get_salt() -> str:
    """Fixed-length salt"""
    return ''.join(random.choice(string.ascii_letters + string.digits) for
                   _ in range(env.get_salt_length()))


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


def add_user(user: User):
    salt = _get_salt()
    hashed_password = hashlib.md5(user.password + salt)

    def task(cursor_factory):
        c = cursor_factory()
        c.execute('''
            INSERT INTO {USER} (
                {ID},
                {HASHED_PASSWORD},
                {SALT},
                {NICKNAME},
                {DESCRIPTION},
                {SIGN_UP_TIME},
                {LAST_ACTIVITY_TIME}
            ) VALUES (
                {id},
                {hashed_password},
                {salt},
                {nickname},
                {description},
                {sign_up_time},
                {last_activity_time}
            )
        '''.format(
            USER=TBL_USER,
            ID=COL_USER_ID,
            HASHED_PASSWORD=COL_USER_HASHED_PASSWORD,
            SALT=COL_USER_SALT,
            NICKNAME=COL_USER_NICKNAME,
            DESCRIPTION=COL_USER_DESCRIPTION,
            SIGN_UP_TIME=COL_USER_SIGN_UP_TIME,
            LAST_ACTIVITY_TIME=COL_USER_LAST_ACTIVITY_TIME,
            id=user.id_,
            hashed_password=hashed_password,
            salt=salt,
            nickname=user.nickname,
            description=user.description,
            sign_up_time=user.sign_up_time,
            last_activity_time=user.last_activity_time
        ))

    manager.execute(task)
