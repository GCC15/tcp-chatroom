// Abstract base class for all SCRP requests

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

import org.json.JSONObject;

public class ScrpRequest {

    public static class SignUpRequest {
        public JSONObject signUpJSON;

        public JSONObject getSignUpJSON() {
            return signUpJSON;
        }

        public JSONObject setSignUpJSON(int requestID, String userID,
                                                  String userPwd, String userNickname) {
            signUpJSON = new JSONObject().put("req_id", requestID);
            signUpJSON.put("method", "SIGN_UP");
            signUpJSON.put("user_id", userID);
            signUpJSON.put("user_password", userPwd);
            signUpJSON.put("user_nickname", userNickname);
            return signUpJSON;
        }
    }

    public static class LogInRequest {
        public JSONObject logInJSON;

        public JSONObject getLogInJSON() {
            return logInJSON;
        }

        public JSONObject setLogInJSON(int requestID, String userID,
                                                 String userPwd) {
            logInJSON = new JSONObject().put("req_id", requestID);
            logInJSON.put("method", "LOG_IN");
            logInJSON.put("user_id", userID);
            logInJSON.put("user_password", userPwd);
            return logInJSON;
        }
    }

    public static class DeleteUserRequest {
        public JSONObject deleteUserJSON;

        public JSONObject getDeleteUserJSON() {
            return deleteUserJSON;
        }

        public JSONObject setDeleteUserJSON(int requestID,
                                                      String userPwd) {
            deleteUserJSON = new JSONObject().put("req_id", requestID);
            deleteUserJSON.put("method", "DELETE_USER");
            deleteUserJSON.put("user_password", userPwd);
            return deleteUserJSON;
        }
    }

    public static class ChangeUserPasswordRequest {
        public JSONObject changeUserPasswordJSON;

        public JSONObject getChangeUserPasswordJSON() {
            return changeUserPasswordJSON;
        }

        public JSONObject setChangeUserPasswordJSON(int requestID,
                                                     String oldPwd, String newPwd) {
            changeUserPasswordJSON = new JSONObject().put("req_id", requestID);
            changeUserPasswordJSON.put("method", "CHANGE_USER_PASSWORD");
            changeUserPasswordJSON.put("old_user_password", oldPwd);
            changeUserPasswordJSON.put("new_user_password", newPwd);
            return changeUserPasswordJSON;
        }
    }

    public static class ChangeUseNicknameRequest {
        public JSONObject changeUserNicknameJSON;

        public JSONObject getChangeUserNicknameJSON() {
            return changeUserNicknameJSON;
        }

        public JSONObject setChangeUserNicknameJSON(int requestID,
                                                              String userNickname) {
            changeUserNicknameJSON = new JSONObject().put("req_id", requestID);
            changeUserNicknameJSON.put("method", "CHANGE_USER_NICKNAME");
            changeUserNicknameJSON.put("user_nickname", userNickname);
            return changeUserNicknameJSON;
        }
    }

    public static class GetTimeRequest {
        public JSONObject getTimeJSON;

        public JSONObject getGetTimeJSON() {
            return getTimeJSON;
        }

        public JSONObject setGetTimeJSON(int requestID) {
            getTimeJSON = new JSONObject().put("req_id", requestID);
            getTimeJSON.put("method", "GET_TIME");
            return getTimeJSON;
        }
    }

    public static class CreateRoomRequest {
        public JSONObject createRoomJSON;

        public JSONObject getCreateRoomJSON() {
            return createRoomJSON;
        }

        public JSONObject setCreateRoomJSON(int requestID, String roomID,
                                                      String roomNickname,
                                                      Utils.RoomAccessType roomAccess) {
            createRoomJSON = new JSONObject().put("req_id", requestID);
            createRoomJSON.put("method", "CREATE_ROOM");
            createRoomJSON.put("room_id", roomID);
            createRoomJSON.put("room_nickname", roomNickname);
            createRoomJSON.put("room_access", roomAccess);
            return createRoomJSON;
        }
    }

    public static class EnterRoomRequest {
        public JSONObject enterRoomJSON;

        public JSONObject getEnterRoomJSON() {
            return enterRoomJSON;
        }

        public JSONObject setEnterRoomJSON(int requestID, String roomID) {
            enterRoomJSON = new JSONObject().put("req_id", requestID);
            enterRoomJSON.put("method", "Enter_ROOM");
            enterRoomJSON.put("room_id", roomID);
            return enterRoomJSON;
        }
    }

    public static class RemoveRoomRequest {
        public JSONObject removeRoomJSON;

        public JSONObject getRemoveRoomJSON() {
            return removeRoomJSON;
        }

        public JSONObject setRemoveRoomJSON(int requestID, String roomID) {
            removeRoomJSON = new JSONObject().put("req_id", requestID);
            removeRoomJSON.put("method", "Remove_ROOM");
            removeRoomJSON.put("room_id", roomID);
            return removeRoomJSON;
        }
    }

    public static class ChangeRoomAccessRequest {

    }

    public static class ChangeRoomNicknameRequest {

    }

    public static class RemoveUserFromRoomRequest {

    }

    public static class SetAdminRequest {

    }

    public static class RemoveAdminRequest {

    }

    public static class AddFriendRequest {

    }

    public static class RemoveFriendRequest {

    }

    public static class ChangeUserDescriptionRequest {

    }

    public static class ChangeRoomDescriptionRequest {

    }

    public static class GetUserLastActivityTimeRequest {

    }

    public static class SendRoomMessageRequest {

    }

    public static class SendPrivateMessageRequest {

    }

    public static class GetRoomAccessTypeRequest {

    }

    public static class SearchUserRequest {

    }

    public static class SearchRoomRequest {

    }


    public static JSONObject createEnterRoomJSON(int requestID, String roomID) {
        JSONObject enterRoomJSON = new JSONObject().put("req_id", requestID);
        enterRoomJSON.put("method", "Enter_ROOM");
        enterRoomJSON.put("room_id", roomID);
        return enterRoomJSON;
    }

    public static JSONObject createEnterPwdRoomJSON(int requestID, String roomID,
                                                    String roomPassword) {
        JSONObject enterPwdRoomJSON = new JSONObject().put("req_id", requestID);
        enterPwdRoomJSON.put("method", "Enter_ROOM");
        enterPwdRoomJSON.put("room_id", roomID);
        enterPwdRoomJSON.put("room_password", roomPassword);
        return enterPwdRoomJSON;
    }


}
