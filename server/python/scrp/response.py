"""SCRP response representation"""

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

from abc import ABCMeta, abstractmethod

from .names import *


class ScrpResponse(metaclass=ABCMeta):
    """SCRP Response"""

    def __init__(self, err: int):
        self.err = err

    @abstractmethod
    def to_dict(self) -> dict:
        """Represent the response as a dict"""
        raise NotImplementedError


class SignUpResponse(ScrpResponse):
    def __init__(self, err: int):
        super().__init__(err)

    def to_dict(self) -> dict:
        return {KEY_ERR: self.err}


class LogInResponse(ScrpResponse):
    def __init__(self, err: int):
        super().__init__(err)

    def to_dict(self) -> dict:
        return {KEY_ERR: self.err}


class DeleteUserResponse(ScrpResponse):
    def __init__(self, err: int):
        super().__init__(err)

    def to_dict(self) -> dict:
        return {KEY_ERR: self.err}


class ChangeUserPasswordResponse(ScrpResponse):
    def __init__(self, err: int):
        super().__init__(err)

    def to_dict(self) -> dict:
        return {KEY_ERR: self.err}


class GetTimeResponse(ScrpResponse):
    def __init__(self, time: float, err: int):
        super().__init__(err)
        self.time = time

    def to_dict(self) -> dict:
        return {
            KEY_TIME: self.time,
            KEY_ERR: self.err
        }


class CreateRoomResponse(ScrpResponse):
    def __init__(self, err: int):
        super().__init__(err)

    def to_dict(self) -> dict:
        return {KEY_ERR: self.err}
