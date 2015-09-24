"""SCRP error representation"""

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


from .names import *


class ScrpError(Exception):
    def __init__(self, error_number):
        self.error_number = error_number
        super().__init__()


class BadRequestError(ScrpError):
    def __init__(self):
        super().__init__(ERR_BAD_REQUEST)


class UserNotLoggedInError(ScrpError):
    def __init__(self):
        super().__init__(ERR_USER_NOT_LOGGED_IN)


class UserAlreadyLoggedInError(ScrpError):
    def __init__(self):
        super().__init__(ERR_USER_ALREADY_LOGGED_IN)


class InvalidError(ScrpError):
    """A value is invalid"""

    def __init__(self, error_number):
        super().__init__(error_number)


class InvalidUserIdError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_USER_ID)


class InvalidRoomIdError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_ROOM_ID)


class InvalidUserPasswordError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_USER_PASSWORD)


class InvalidRoomPasswordError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_ROOM_PASSWORD)


class InvalidUserNicknameError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_USER_NICKNAME)


class InvalidRoomNicknameError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_ROOM_NICKNAME)


class InvalidUserDescriptionError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_USER_DESCRIPTION)


class InvalidRoomDescriptionError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_ROOM_DESCRIPTION)


class InvalidRoomAccessTypeError(InvalidError):
    def __init__(self):
        super().__init__(ERR_INVALID_ROOM_ACCESS_TYPE)


class UserAlreadyExistsError(ScrpError):
    def __init__(self):
        super().__init__(ERR_USER_ALREADY_EXISTS)


class RoomAlreadyExistsError(ScrpError):
    def __init__(self):
        super().__init__(ERR_ROOM_ALREADY_EXISTS)


class TooManyWrongAttemptsError(ScrpError):
    def __init__(self):
        super().__init__(ERR_TOO_MANY_WRONG_ATTEMPTS)


class IdPasswordNotMatchError(ScrpError):
    def __init__(self):
        super().__init__(ERR_ID_PASSWORD_NOT_MATCH)


class ForbiddenError(ScrpError):
    def __init__(self):
        super().__init__(ERR_FORBIDDEN)


class Success(ScrpError):
    def __init__(self):
        super().__init__(ERR_SUCCESS)


class UnknownError(ScrpError):
    def __init__(self):
        super().__init__(ERR_UNKNOWN)
