// Room class

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

public class Room {
    private String roomID;
    private String roomNickname;
    private String roomDescription;
    private User roomOwner;
    private HashSet<User> roomAdmins;
    private HashSet<User> roomMembers;
    Utils.RoomAccessType roomAccessType;

    public Room(String ID, String nickname, String description, User owner,
                Utils.RoomAccessType accessType) {
        roomID = ID;
        roomNickname = nickname;
        roomDescription = description;
        roomOwner = owner;
        roomAdmins = new HashSet<>();
        roomAdmins.add(owner);
        roomMembers = new HashSet<>();
        roomMembers.add(owner);
        roomAccessType = accessType;
    }

    public String getRoomIDID() { return roomID; }

    public void setRoomID(String ID) { roomID = ID; }

    public String getRoomNickname() { return roomNickname; }

    public void setRoomNickname(String nickname) { roomNickname = nickname; }

    public String getRoomDescription() { return roomDescription; }

    public void setRoomDescription(String description) { roomDescription = description; }

    public User getRoomOwner() { return roomOwner; }

    public void setRoomOwner(User owner) { roomOwner = owner; }

    public HashSet<User> getRoomAdmins(){
        return roomAdmins;
    }

    public void addAdmin(User admin){
        roomAdmins.add(admin);
    }

    public void removeAdmin(User friend){
        roomAdmins.remove(friend);
    }

    public void removeAllAdmins(){
        roomAdmins.clear();
    }

    public HashSet<User> getRoomMembers(){
        return roomMembers;
    }

    public void addMember(User member){
        roomMembers.add(member);
    }

    public void removeMember(User member){
        roomMembers.remove(member);
    }

    public void removeAllMembers() {
        roomMembers.clear();
    }

    public void setRoomAccessType(Utils.RoomAccessType accessType) {
        roomAccessType = accessType;
    }

    public Utils.RoomAccessType getRoomAccessType(){
        return roomAccessType;
    }

}
