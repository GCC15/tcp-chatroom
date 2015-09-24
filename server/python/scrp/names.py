"""Constants in SCRP"""

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

# Error numbers
ERR_BAD_REQUEST = 233
ERR_USER_NOT_LOGGED_IN = 250
ERR_USER_ALREADY_LOGGED_IN = 251
ERR_INVALID_USER_ID = 300
ERR_INVALID_ROOM_ID = 301
ERR_INVALID_USER_PASSWORD = 310
ERR_INVALID_ROOM_PASSWORD = 311
ERR_INVALID_USER_NICKNAME = 320
ERR_INVALID_ROOM_NICKNAME = 321
ERR_INVALID_USER_DESCRIPTION = 330
ERR_INVALID_ROOM_DESCRIPTION = 331
ERR_INVALID_ROOM_ACCESS_TYPE = 340
ERR_USER_ALREADY_EXISTS = 400
ERR_ROOM_ALREADY_EXISTS = 401
ERR_TOO_MANY_WRONG_ATTEMPTS = 402
ERR_ID_PASSWORD_NOT_MATCH = 403
ERR_FORBIDDEN = 801
ERR_SUCCESS = 900
ERR_UNKNOWN = 999

# Fields
KEY_METHOD = 'method'
KEY_USER_ID = 'user_id'
KEY_USER_PASSWORD = 'user_password'
KEY_USER_NICKNAME = 'user_nickname'
KEY_OLD_USER_PASSWORD = 'old_user_password'
KEY_NEW_USER_PASSWORD = 'new_user_password'

# Request methods
REQ_SIGN_UP = 'sign_up'
REQ_LOG_IN = 'log_in'
REQ_DELETE_USER = 'delete_user'
REQ_CHANGE_USER_PASSWORD = 'change_user_password'
REQ_GET_TIME = 'get_time'
REQ_CREATE_ROOM = 'create_room'

# Push methods
