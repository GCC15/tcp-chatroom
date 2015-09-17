"""Data access object"""

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
import sqlite3

import env
import logger
from .names import *
from scrp.entity import *

DB_VERSION = 1  # Current DB version

_var_dir = env.get_var_dir()
env.make_dirs(_var_dir)
_db_file = env.get_db_file()
_db_file_path = os.path.join(_var_dir, _db_file)


def _do_upgrade():
    """
    Upgrade the database if necessary.
    See CHANGELOG for changes made in each version.
    """
    dao = Dao()
    existing_ver = dao.get_db_version()
    if existing_ver > DB_VERSION:
        logger.e('DB version ({}) is older than the existing version ({})!'
                 .format(DB_VERSION, existing_ver))
    elif existing_ver < DB_VERSION:
        logger.w('DB needs to upgrade from version {} to {}'
                 .format(existing_ver, DB_VERSION))
        input('Press enter to continue...')
        dao.upgrade_db(existing_ver, DB_VERSION)
        dao.set_db_version(DB_VERSION)
        dao.commit()
        logger.i('DB upgrade complete!')


class Dao:
    def __init__(self):
        self.__conn = sqlite3.connect(_db_file_path)
        self.__conn.row_factory = sqlite3.Row

    def commit(self):
        """Commit transaction so other connections know"""
        self.__conn.commit()

    def close(self):
        """Close the DB connection. All uncommitted changes will be lost!"""
        self.__conn.close()

    def test(self):
        """For testing"""
        c = self.__conn.cursor()
        c.execute('SELECT ?', [42])
        return c.fetchone()[0]

    def upgrade_db(self, old_ver: int, new_ver: int):
        """Perform the upgrade of the database recursively"""
        assert old_ver <= new_ver
        c = self.__conn.cursor()
        if old_ver != new_ver:
            if old_ver == 0:  # DB is empty
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
                logger.e('Cannot upgrade DB from {} to {}!'
                         .format(old_ver, old_ver + 1))
            # Do the rest
            self.upgrade_db(old_ver + 1, new_ver)

    def get_db_version(self) -> int:
        """Get the existing database version"""
        c = self.__conn.cursor()
        c.execute('PRAGMA user_version')
        return c.fetchone()[0]

    def set_db_version(self, version: int):
        """Set the new database version"""
        c = self.__conn.cursor()
        c.execute('PRAGMA user_version = {}'.format(version))

    def create_user(self, user: User):
        """Create a new user"""
        c = self.__conn.cursor()
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
            hashed_password=user.hashed_password,
            salt=user.salt,
            nickname=user.nickname,
            description=user.description,
            sign_up_time=user.sign_up_time,
            last_activity_time=user.last_activity_time
        ))

    def find_user(self, user_id: str) -> User:
        """
        Return the user with given user_id; return None if not found.
        user_id should be validated beforehand.
        """
        c = self.__conn.cursor()
        c.execute(
            'SELECT * FROM {USER} WHERE {ID} = ?'.format(
                USER=TBL_USER
            ), [user_id]
        )
        row = c.fetchone()
        if not row:
            return None
        return User(
            row[COL_USER_ID],
            row[COL_USER_HASHED_PASSWORD],
            row[COL_USER_NICKNAME],
            row[COL_USER_DESCRIPTION],
            row[COL_USER_SIGN_UP_TIME],
            row[COL_USER_LAST_ACTIVITY_TIME],
            row[COL_USER_SALT]
        )

    def update_user(self, user: User):
        c = self.__conn.cursor()


_do_upgrade()


def main():
    dao = Dao()
    print(dao.test())


if __name__ == '__main__':
    main()
