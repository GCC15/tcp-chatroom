"""
SCRP entity representation and validation.
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

import re

from .error import *


class User:
    PATTERN_ID = re.compile(r'^\w{1,16}$', re.A)
    PATTERN_PASSWORD = re.compile(r'^[ -~]{6,64}$', re.A)

    @staticmethod
    def is_valid_id(id_: str) -> bool:
        return User.PATTERN_ID.match(id_)

    @staticmethod
    def is_valid_password(password: str) -> bool:
        return User.PATTERN_PASSWORD.match(password)

    @staticmethod
    def is_valid_nickname(nickname: str) -> bool:
        return 1 <= len(nickname) <= 32

    @staticmethod
    def is_valid_description(description: str) -> bool:
        return len(description) <= 256

    def __init__(self, id_: str, password: str, nickname: str, description: str,
                 sign_up_time: int, last_activity_time: int):
        if not self.is_valid_id(id_):
            raise InvalidUserIdError()
        if not self.is_valid_password(password):
            raise InvalidUserPasswordError()
        if not self.is_valid_nickname(nickname):
            raise InvalidUserNicknameError()
        if not self.is_valid_description(description):
            raise InvalidUserDescriptionError()
        self.id_ = id_
        self.password = password
        self.nickname = nickname
        self.description = description
        self.sign_up_time = sign_up_time
        self.last_activity_time = last_activity_time


class Room:
    def __init__(self, id_: str, nickname: str, description: str):
        pass


class RoomMessage:
    def __init__(self):
        pass


class PrivateMessage:
    def __init__(self):
        pass


class Friendship:
    def __init__(self):
        pass
