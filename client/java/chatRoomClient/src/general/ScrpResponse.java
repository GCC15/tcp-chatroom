// Abstract base class for all SCRP response

// Copyright (C) 2015 Zhang NS, Zifan Li, Zichao Li

// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License along
// with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

package general;

public class ScrpResponse {

    public static class SignUpResponse {

    }

    public static class LogInResponse {

    }

    public static class DeleteUserResponse {

    }

    public static class ChangeUserPasswordResponse {

    }

    public static class ChangeUseNicknameResponse {

    }

    public static class GetTimeResponse {

    }

    public static class CreateRoomResponse {

    }

    public static class EnterRoomResponse {

    }

    public static class RemoveRoomResponse {

    }

    public static class ChangeRoomAccessResponse {

    }

    public static class ChangeRoomNicknameResponse {

    }

    public static class RemoveUserFromRoomResponse {

    }

    public static class SetAdminResponse {

    }

    public static class RemoveAdminResponse {

    }

    public static class AddFriendResponse {

    }

    public static class RemoveFriendResponse {

    }

    public static class ChangeUserDescriptionResponse {

    }

    public static class ChangeRoomDescriptionResponse {

    }

    public static class GetUserLastActivityTimeResponse {

    }

    public static class SendRoomMessageResponse {

    }

    public static class SendPrivateMessageResponse {

    }

    public static class GetRoomAccessTypeResponse {

    }

    public static class SearchUserResponse {

    }

    public static class SearchRoomRequest {

    }
    private int responseID;

    public ScrpResponse(int ID) {
        responseID = ID;
    }
}
