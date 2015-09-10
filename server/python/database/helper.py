"""Database helper routines"""

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
from .names import *


def get_db_version() -> int:
    """Get the database version"""

    def get_version_task(cursor_factory) -> int:
        c = cursor_factory()
        c.execute('PRAGMA user_version')
        return c.fetchone()[0]

    return manager.execute(get_version_task)


def set_db_version(version: int):
    """Set a new database version"""

    def set_version_task(cursor_factory):
        c = cursor_factory()
        c.execute('PRAGMA user_version = {}'.format(version))

    manager.execute(set_version_task)


def upgrade_db(old_ver: int, new_ver: int):
    """Perform the upgrade of the database recursively"""
    assert old_ver <= new_ver
    if old_ver != new_ver:
        def increment_task(cursor_factory):
            """Upgrade from old_ver to old_ver + 1"""
            c = cursor_factory()
            if old_ver == 0: # DB is empty
                # User
                c.execute('''
                    CREATE TABLE {user} (
                        {id} TEXT NOT NULL PRIMARY KEY,
                        {password} TEXT NOT NULL,
                        {salt} TEXT NOT NULL,
                        {nickname} TEXT NOT NULL,
                        {description} TEXT NOT NULL,
                        {sign_up_time} INTEGER NOT NULL
                    )
                '''.format(
                    user=TBL_USER,
                    id=COL_USER_ID,
                    password=COL_USER_PASSWORD,
                    salt=COL_USER_SALT,
                    nickname=COL_USER_NICKNAME,
                    description=COL_USER_DESCRIPTION,
                    sign_up_time=COL_USER_SIGN_UP_TIME,
                    last_activity_time=COL_USER_LAST_ACTIVITY_TIME
                ))
                # Room
                c.execute('''
                    CREATE TABLE {room} (
                        {id} TEXT NOT NULL PRIMARY KEY,
                        {nickname} TEXT NOT NULL,
                        {description} TEXT NOT NULL,
                        {owner} TEXT NOT NULL,
                        {password} TEXT,
                        {access_type} INTEGER NOT NULL
                    )
                '''.format(
                    room=TBL_ROOM,
                    id=COL_ROOM_ID,
                    nickname=COL_ROOM_NICKNAME,
                    description=COL_ROOM_DESCRIPTION,
                    owner=COL_ROOM_OWNER,
                    password=COL_ROOM_PASSWORD,
                    access_type=COL_ROOM_ACCESS_TYPE
                ))
            elif old_ver == 1:
                pass
            else:
                raise ValueError('Cannot upgrade DB from {} to {}!'
                                 .format(old_ver, old_ver + 1))

        manager.execute(increment_task)
        # Do the rest
        upgrade_db(old_ver + 1, new_ver)
