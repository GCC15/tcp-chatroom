"""String constants for the SQLite database"""

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
COL_USER_PASS = 'pass'
COL_USER_SALT = 'salt'
COL_USER_SIGN_UP_TIME = 'sign_up_time'
COL_USER_NICKNAME = 'name'
COL_USER_DESC = 'desc'

# Rooms
TBL_ROOM = 'room'
COL_ROOM_ID = 'id'
COL_ROOM_NICKNAME = 'name'
COL_ROOM_DESC = 'desc'

# Friendships
TBL_FRIENDSHIP = 'friendship'
COL_FRIEND_L = 'user_l'
COL_FRIEND_R = 'user_r'

# Messages
TBL_MSG = 'msg'
COL_MSG_ID = 'id'
COL_MSG_TIME = 'time'
COL_MSG_CONTENT = 'content'
COL_MSG_SENDER = 'sender'
COL_MSG_ROOM = 'room'

# Friend requests
TBL_FRIEND_REQ = 'friend_req'
COL_FRIEND_REQ_TIME = 'time'
COL_FRIEND_REQ_FROM = 'user_from'
COL_FRIEND_REQ_TO = 'user_to'
