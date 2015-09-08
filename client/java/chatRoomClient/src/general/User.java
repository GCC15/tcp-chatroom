// User class

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

import java.util.*;

public class User {
    private String userID;
    private String userNickname;
    private String userDescription;
    private int userSignUpTime;
    private int userLastActivityTime;
    private HashSet<User> userFriends;
    private HashSet<Room> userRooms;
    Utils.AllUserMode userMode;

    public User(String ID, String nickname, String description) {
        userID = ID;
        userNickname = nickname;
        userDescription = description;
    }

    public String getUserID() { return userID; }

    public void setUserID(String ID) { userID = ID; }

    public String getUserNickname() { return userNickname; }

    public void setUserNickname(String nickname) { userNickname = nickname; }

    public String getUserDescription() { return userDescription; }

    public void setUserDescription(String description) { userDescription = description; }

    public int getUserSignUpTime(){
        return userSignUpTime;
    }

    public void setUserSignUpTime(int signUpTime){
        userSignUpTime = signUpTime;
    }

    public int getUserLastActivityTime(){
        return userLastActivityTime;
    }

    public void setUserLastActivityTime(int lastActivityTime){
        userLastActivityTime = lastActivityTime;
    }

    public HashSet<User> getUserFriendList(){
        return userFriends;
    }

    public void addFriend(User friend){
        userFriends.add(friend);
    }

    public void removeFriend(User friend){
        userFriends.remove(friend);
    }

    public void removeAllFriends(){
        userFriends.clear();
    }

    public HashSet<Room> getUserRoomList(){
        return userRooms;
    }

    public void addRoom(Room room){
        userRooms.add(room);
    }

    public void removeRoom(Room room){
        userRooms.remove(room);
    }

    public void removeAllRooms() {
        userFriends.clear();
    }

    public void setUserMode(Utils.AllUserMode mode) {
        userMode = mode;
    }

    public Utils.AllUserMode getUserMode(){
        return userMode;
    }
}
