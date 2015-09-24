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

    req_method = None  # to be overridden

    def get_handler(self):
        return _method_dict[self.req_method]

    @staticmethod
    def from_dict(req_dict: dict):
        """
        Factory method to create an ScrpRequest object from a given dict.
        """
        if type(req_dict) != dict or KEY_METHOD not in req_dict:
            # Request method cannot be determined
            raise InvalidRequestDictError
        req_method = req_dict[KEY_METHOD]
        if req_method not in _method_dict:
            # Unknown request method
            raise InvalidRequestDictError
        # Dispatch req_dict to the specific constructor
        return _get_request_class_from_method(req_method)(req_dict)


class SignUpRequest(ScrpRequest):
    req_method = REQ_SIGN_UP

    def __init__(self, req_dict: dict):
        super().__init__()
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
        super().__init__()
        try:
            self.user_id = req_dict[KEY_USER_ID]
            self.user_password = req_dict[KEY_USER_PASSWORD]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class DeleteUserRequest(ScrpRequest):
    req_method = REQ_DELETE_USER

    def __init__(self, req_dict: dict):
        super().__init__()
        try:
            self.user_password = req_dict[KEY_USER_PASSWORD]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class ChangeUserPasswordRequest(ScrpRequest):
    req_method = REQ_CHANGE_USER_PASSWORD

    def __init__(self, req_dict: dict):
        super().__init__()
        try:
            self.old_user_password = req_dict[KEY_OLD_USER_PASSWORD]
            self.new_user_password = req_dict[KEY_NEW_USER_PASSWORD]
        except Exception as e:
            logger.e(str(e))
            raise InvalidRequestDictError


class GetTimeRequest(ScrpRequest):
    req_method = REQ_GET_TIME

    def __init__(self, req_dict: dict):
        super().__init__()


class CreateRoomRequest(ScrpRequest):
    req_method = REQ_CREATE_ROOM

    def __init__(self, req_dict):
        super().__init__()
        # TODO


# TODO: More request methods

# Map from request method to list [request_cls, handler_cls]
_method_dict = {}

# Iterate each subclass defined previously to fill the dict
for request_cls in ScrpRequest.__subclasses__():
    _method_dict[request_cls.METHOD] = [request_cls, None]


def set_request_handler(req_method: str, handler_cls: type):
    """Set the handler class for the given request method"""
    assert req_method in _method_dict
    _method_dict[req_method][1] = handler_cls


class RequestMethodNotFoundError(ValueError):
    """Cannot find the request method specified"""


def _get_request_class_from_method(req_method: str) -> type:
    if req_method not in _method_dict:
        raise RequestMethodNotFoundError
    return _method_dict[req_method][0]


def _get_request_handler_from_method(req_method: str) -> type:
    if req_method not in _method_dict:
        raise RequestMethodNotFoundError
    return _method_dict[req_method][1]
