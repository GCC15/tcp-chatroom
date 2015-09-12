"""SCRP request representation"""


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

class ScrpRequest:
    """SCRP Request"""


class SignUpRequest(ScrpRequest):
    def __init__(self, user_id: str, user_password: str, user_nickname: str):
        super().__init__()
        self.user_id = user_id
        self.user_password = user_password
        self.user_nickname = user_nickname


class LogInRequest(ScrpRequest):
    def __init__(self, user_id: str, user_password: str):
        super().__init__()
        self.user_id = user_id
        self.User_password = user_password


class DeleteUserRequest(ScrpRequest):
    def __init__(self, user_password: str):
        super().__init__()
        self.user_password = user_password


class ChangeUserPasswordRequest(ScrpRequest):
    def __init__(self, old_user_password: str, new_user_password: str):
        super().__init__()
        self.old_user_password = old_user_password
        self.new_user_password = new_user_password


class GetTimeRequest(ScrpRequest):
    def __init__(self):
        super().__init__()


class CreateRoomRequest(ScrpRequest):
    def __init__(self, room_id: str, room_nickname: str, room_access: int,
                 room_password: str = None):
        super().__init__()
        self.room_id = room_id
        self.room_nickname = room_nickname
        self.room_access = room_access
        self.room_password = room_password
