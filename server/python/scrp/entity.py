"""
SCRP entity representation and validation.

An entity class, e.g. User, contains
(1) Static methods for validating each fields (named validate_xxx).
    Raise a subclass of ScrpError if the field is invalid.
(2) A constructor.
    Receives necessary fields to construct an instance object. A subclass of
    ScrpError is raised if a field is invalid.
(3) Other instance methods.
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

from database import utils
from .error import *


class User:
    PATTERN_ID = re.compile(r'^\w{1,16}$', re.A)
    PATTERN_PASSWORD = re.compile(r'^[ -~]{6,64}$', re.A)

    @staticmethod
    def validate_id(id_: str):
        if not User.PATTERN_ID.match(id_):
            raise InvalidUserIdError

    @staticmethod
    def validate_password(password: str):
        if not User.PATTERN_PASSWORD.match(password):
            raise InvalidUserPasswordError

    @staticmethod
    def validate_nickname(nickname: str):
        if not 1 <= len(nickname) <= 32:
            raise InvalidUserNicknameError

    @staticmethod
    def validate_description(description: str):
        if not len(description) <= 256:
            raise InvalidUserDescriptionError

    def is_password_correct(self, password: str) -> bool:
        return utils.salted_hash(password, self.salt) == self.hashed_password

    def __init__(self, id_: str, password: str, nickname: str, description: str,
                 sign_up_time: int, last_activity_time: int, salt: str = None):
        """If password has been salt-hashed, also give the salt"""
        self.validate_id(id_)
        if salt is None:
            self.validate_password(password)
        self.validate_nickname(nickname)
        self.validate_description(description)
        self.id_ = id_
        if salt:
            self.salt = salt
            self.hashed_password = password
        else:
            self.salt = utils.generate_salt()
            self.hashed_password = utils.salted_hash(password, self.salt)
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
