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

import java.net.*;
import java.io.*;

public class ScrpRequest {
    private int requestID;
    private String requestMethod;

    public ScrpRequest(int ID, String method) {
        requestID = ID;
        requestMethod = method;
    }

    // NOTE: Everything below must not be useful or correct


    public JSONObject createSignUpJSON(String userID, String userPwd, String userNickname) {
        assert (requestMethod.equals("SIGN_UP"));
        JSONObject signUpJSON = new JSONObject().put("req_id", requestID);
        signUpJSON.put("method", requestMethod);
        signUpJSON.put("user_id", userID);
        signUpJSON.put("user_password", userPwd);
        signUpJSON.put("user_nickname", userNickname);
        return signUpJSON;
    }

    public JSONObject createLogInJSON(String userID, String userPwd) {
        assert (requestMethod.equals("LOG_IN"));
        JSONObject logInJSON = new JSONObject().put("req_id", requestID);
        logInJSON.put("method", requestMethod);
        logInJSON.put("user_id", userID);
        logInJSON.put("user_password", userPwd);
        return logInJSON;
    }
}
