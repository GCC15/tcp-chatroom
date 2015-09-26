"""
Request handlers
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

from abc import ABCMeta, abstractmethod
from database.dao import Dao

import logger
from scrp.names import *
from scrp.request import ScrpRequest
from scrp.response import ScrpResponse


class RequestHandler(metaclass=ABCMeta):
    def __init__(self):
        self.__dao = None

    def get_dao(self) -> Dao:
        """DAO singleton"""
        if not self.__dao:
            self.__dao = Dao()
        return self.__dao

    @abstractmethod
    def handle_request(self, req: ScrpRequest) -> ScrpResponse:
        """Handle a request synchronously"""
        raise NotImplementedError


class SignUpRequestHandler(RequestHandler):
    def __init__(self):
        super().__init__()

    def handle_request(self, req: ScrpRequest) -> ScrpResponse:
        pass


class LogInRequestHandler(RequestHandler):
    def __init__(self):
        super().__init__()

    def handle_request(self, req: ScrpRequest) -> ScrpResponse:
        pass
