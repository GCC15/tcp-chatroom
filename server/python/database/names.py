"""String constants for the database"""

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

# Users
TBL_USER = 'user'
COL_USER_ID = 'id'
COL_USER_PASSWORD = 'password'
COL_USER_SALT = 'salt'
COL_USER_NICKNAME = 'nickname'
COL_USER_DESCRIPTION = 'description'
COL_USER_SIGN_UP_TIME = 'sign_up_time'
COL_USER_LAST_ACTIVITY_TIME = 'last_activity_time'

# Rooms
TBL_ROOM = 'room'
COL_ROOM_ID = 'id'
COL_ROOM_NICKNAME = 'nickname'
COL_ROOM_DESCRIPTION = 'description'
COL_ROOM_OWNER = 'owner'
COL_ROOM_PASSWORD = 'password'
COL_ROOM_ACCESS_TYPE = 'access_type'

# Members
TBL_MEMBER = 'member'
COL_MEMBER_USER_ID = 'user_id'
COL_MEMBER_ROOM_ID = 'room_id'
COL_MEMBER_IS_ADMIN = 'is_admin'

# Friends
TBL_FRIEND = 'friend'
COL_FRIEND_USER_L = 'user_l'
COL_FRIEND_USER_R = 'user_r'

# Friend requests
TBL_FRIEND_REQUEST = 'friend_req'
COL_FRIEND_REQUEST_TIME = 'time'
COL_FRIEND_REQUEST_FROM = 'user_from'
COL_FRIEND_REQUEST_TO = 'user_to'

# Messages
TBL_MESSAGE = 'message'
COL_MESSAGE_ID = 'id'
COL_MESSAGE_TIME = 'time'
COL_MESSAGE_CONTENT = 'content'
COL_MESSAGE_SENDER = 'sender'
COL_MESSAGE_ROOM = 'room'
