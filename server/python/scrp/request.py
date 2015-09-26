"""SCRP request representation and basic validation"""

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

import logger
from .names import *


class InvalidRequestDictError(ValueError):
    """
    The request dict is invalid.
    Possible causes:
        The request method is unknown.
        One or more necessary fields are missing.
    """


class ScrpRequest:
    """SCRP Request"""

    def __init__(self, req_dict: dict):
        """Do not instantiate directly"""
        try:
            self.req_id = req_dict[KEY_REQ_ID]
            if type(self.req_id) != int:
                raise TypeError
        except Exception as e:
            logger.e(e)
            raise InvalidRequestDictError

    def get_handler_cls(self) -> type:
        # noinspection PyUnresolvedReferences
        return _get_request_handler(self.req_method)

    @staticmethod
    def from_dict(req_dict: dict) -> 'ScrpRequest':
        """
        Factory method to create an ScrpRequest object from a given dict.
        """
        try:
            # Dispatch req_dict to the specific constructor
            return _get_request_class(req_dict[KEY_METHOD])(req_dict)
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class SignUpRequest(ScrpRequest):
    req_method = REQ_SIGN_UP

    def __init__(self, req_dict: dict):
        super().__init__(req_dict)
        try:
            self.user_id = req_dict[KEY_USER_ID]
            self.user_password = req_dict[KEY_USER_PASSWORD]
            self.user_nickname = req_dict[KEY_USER_NICKNAME]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class LogInRequest(ScrpRequest):
    req_method = REQ_LOG_IN

    def __init__(self, req_dict: dict):
        super().__init__(req_dict)
        try:
            self.user_id = req_dict[KEY_USER_ID]
            self.user_password = req_dict[KEY_USER_PASSWORD]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class DeleteUserRequest(ScrpRequest):
    req_method = REQ_DELETE_USER

    def __init__(self, req_dict: dict):
        super().__init__(req_dict)
        try:
            self.user_password = req_dict[KEY_USER_PASSWORD]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class ChangeUserPasswordRequest(ScrpRequest):
    req_method = REQ_CHANGE_USER_PASSWORD

    def __init__(self, req_dict: dict):
        super().__init__(req_dict)
        try:
            self.old_user_password = req_dict[KEY_OLD_USER_PASSWORD]
            self.new_user_password = req_dict[KEY_NEW_USER_PASSWORD]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class GetTimeRequest(ScrpRequest):
    req_method = REQ_GET_TIME

    def __init__(self, req_dict: dict):
        super().__init__(req_dict)


class CreateRoomRequest(ScrpRequest):
    req_method = REQ_CREATE_ROOM

    def __init__(self, req_dict: dict):
        super().__init__(req_dict)
        # TODO


# TODO: More request methods

# Map from request method to list [request_cls, handler_cls]
_method_dict = {}

# Iterate each subclass defined previously to fill the dict
for request_cls in ScrpRequest.__subclasses__():
    _method_dict[request_cls.METHOD] = [request_cls, None]


def _get_request_class(req_method: str) -> type:
    return _method_dict[req_method][0]


def _get_request_handler(req_method: str) -> type:
    assert req_method in _method_dict
    return _method_dict[req_method][1]


def set_request_handler(req_method: str, handler_cls: type):
    """Set the handler class for the given request method"""
    assert req_method in _method_dict
    _method_dict[req_method][1] = handler_cls
