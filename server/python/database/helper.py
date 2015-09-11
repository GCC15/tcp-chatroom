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
                    CREATE TABLE {USER} (
                        {ID} TEXT NOT NULL PRIMARY KEY,
                        {HASHED_PASSWORD} TEXT NOT NULL,
                        {SALT} TEXT NOT NULL,
                        {NICKNAME} TEXT NOT NULL,
                        {DESCRIPTION} TEXT NOT NULL,
                        {SIGN_UP_TIME} INTEGER NOT NULL,
                        {LAST_ACTIVITY_TIME} INTEGER NOT NULL
                    )
                '''.format(
                    USER=TBL_USER,
                    ID=COL_USER_ID,
                    HASHED_PASSWORD=COL_USER_HASHED_PASSWORD,
                    SALT=COL_USER_SALT,
                    NICKNAME=COL_USER_NICKNAME,
                    DESCRIPTION=COL_USER_DESCRIPTION,
                    SIGN_UP_TIME=COL_USER_SIGN_UP_TIME,
                    LAST_ACTIVITY_TIME=COL_USER_LAST_ACTIVITY_TIME
                ))
                # Room
                c.execute('''
                    CREATE TABLE {ROOM} (
                        {ID} TEXT NOT NULL PRIMARY KEY,
                        {NICKNAME} TEXT NOT NULL,
                        {DESCRIPTION} TEXT NOT NULL,
                        {OWNER} TEXT NOT NULL,
                        {PASSWORD} TEXT,
                        {ACCESS_TYPE} INTEGER NOT NULL
                    )
                '''.format(
                    ROOM=TBL_ROOM,
                    ID=COL_ROOM_ID,
                    NICKNAME=COL_ROOM_NICKNAME,
                    DESCRIPTION=COL_ROOM_DESCRIPTION,
                    OWNER=COL_ROOM_OWNER,
                    PASSWORD=COL_ROOM_PASSWORD,
                    ACCESS_TYPE=COL_ROOM_ACCESS_TYPE
                ))
            elif old_ver == 1:
                pass
            else:
                raise ValueError('Cannot upgrade DB from {} to {}!'
                                 .format(old_ver, old_ver + 1))

        manager.execute(increment_task)
        # Do the rest
        upgrade_db(old_ver + 1, new_ver)
