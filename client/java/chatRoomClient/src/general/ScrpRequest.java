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

    public static abstract class BaseRequest {
        private int requestID;
        private String requestMethod;

        private BaseRequest(int ID, String method) {
            requestID = ID;
            requestMethod = method;
        }

        public int getRequestID() {
            return requestID;
        }

        public String getMethod() {
            return requestMethod;
        }

        public JSONObject createJSON() {
            JSONObject json = new JSONObject().put("req_id", requestID);
            json.put("method", requestMethod);
            return json;
        }
    }

    public static class SignUpRequest extends BaseRequest {
        private String userID;
        private String userPwd;
        private String userNickname;

        public SignUpRequest(int requestID, String userID,
                             String userPwd, String userNickname) {
            super(requestID, "SIGN_UP");
            this.userID = userID;
            this.userPwd = userPwd;
            this.userNickname = userNickname;
        }

        public String getUserID() {
            return userID;
        }

        public String getUserNickname() {
            return userNickname;
        }

        @Override
        public JSONObject createJSON() {
            JSONObject signUpJSON = super.createJSON();
            signUpJSON.put("user_id", userID);
            signUpJSON.put("user_password", userPwd);
            signUpJSON.put("user_nickname", userNickname);
            return signUpJSON;
        }
    }

    public static class LogInRequest extends BaseRequest {
        private String userID;
        private String userPwd;

        public LogInRequest(int requestID, String userID,
                            String userPwd) {
            super(requestID, "LOG_IN");
            this.userID = userID;
            this.userPwd = userPwd;
        }

        public String getUserID() {
            return userID;
        }

        @Override
        public JSONObject createJSON() {
            JSONObject logInJSON = super.createJSON();
            logInJSON.put("user_id", userID);
            logInJSON.put("user_password", userPwd);
            return logInJSON;
        }
    }

    public static class DeleteUserRequest extends BaseRequest {
        private String userPwd;

        public DeleteUserRequest(int requestID, String userPwd) {
            super(requestID, "DELETE_USER");
            this.userPwd = userPwd;
        }

        @Override
        public JSONObject createJSON() {
            JSONObject deleteUserJSON = super.createJSON();
            deleteUserJSON.put("user_password", userPwd);
            return deleteUserJSON;
        }
    }

    public static class ChangeUserPasswordRequest extends BaseRequest {
        private String oldPwd;
        private String newPWd;

        public ChangeUserPasswordRequest(int requestID, String oldPwd,
                                         String newPWd) {
            super(requestID, "CHANGE_USER_PASSWORD");
            this.oldPwd = oldPwd;
            this.newPWd = newPWd;
        }

        @Override
        public JSONObject createJSON() {
            JSONObject changeUserPasswordJSON = super.createJSON();
            changeUserPasswordJSON.put("old_user_password", oldPwd);
            changeUserPasswordJSON.put("new_user_password", newPWd);
            return changeUserPasswordJSON;
        }
    }

    public static class ChangeUserNicknameRequest extends BaseRequest {
        private String userNickname;

        public ChangeUserNicknameRequest(int requestID, String userNickname) {
            super(requestID, "CHANGE_USER_NICKNAME");
            this.userNickname = userNickname;
        }

        public String getUserNickname(){
            return userNickname;
        }

        @Override
        public JSONObject createJSON() {
            JSONObject changeUserNicknameJSON = super.createJSON();
            changeUserNicknameJSON.put("user_nickname", userNickname);
            return changeUserNicknameJSON;
        }
    }

    public static class GetTimeRequest extends BaseRequest {

        public GetTimeRequest(int requestID){
            super(requestID, "GET_TIME");
        }

        @Override
        public JSONObject createJSON() {
            JSONObject getTimeJson = super.createJSON();
            return getTimeJson;
        }
    }

    public static class CreateRoomRequest extends BaseRequest{
        private String roomID;
        private String roomNickname;
        private Utils.RoomAccessType roomAccess;

        public CreateRoomRequest(int requestID, String roomID,
                                 String roomNickname,
                                 Utils.RoomAccessType roomAccess){
            super(requestID,"CREATE_ROOM");
            this.roomID = roomID;
            this.roomNickname = roomNickname;
            this.roomAccess = roomAccess;
        }

        public String getRoomID(){
            return roomID;
        }

        public String getRoomNickname(){
            return roomNickname;
        }

        public Utils.RoomAccessType getRoomAccess(){
            return roomAccess;
        }

        @Override
        public JSONObject createJSON() {
            JSONObject createRoomJSON = super.createJSON();
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
