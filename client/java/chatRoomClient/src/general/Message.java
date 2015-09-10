// Message class, base class for PrivateMessage class and RoomMessage class

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

public class Message {
    private String messageId;
    private int messageServerReceivedTime;
    private User messageSender;

    public Message(String ID, int time, User sender) {
        messageId = ID;
        messageServerReceivedTime = time;
        messageSender = sender;
    }

    public String getMessageID() {
        return messageId;
    }

    public void setMessageID(String ID) {
        messageId = ID;
    }

    public int getMessageServerReceivedTime() {
        return messageServerReceivedTime;
    }

    public void setMessageServerReceivedTime(int time) {
        messageServerReceivedTime = time;
    }

    public User getMessageSender() {
        return messageSender;
    }

    public void setMessageSender(User sender) {
        messageSender = sender;
    }

}
