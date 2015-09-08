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

import java.time.LocalDateTime;

public class Client {
    private String clientNickname;
    public static final String clientVersion = Strings.CLIENT_VERSION;
    private String clientDescription;
    public static final String protocolVersion = Strings.SCRP_VERSION;
    private int clientTime;

    public Client(String nickname, String description) {
        clientNickname = nickname;
        clientDescription = description;
    }

    public String getClientNickname() {
        return clientNickname;
    }

    public void setClientNickname(String nickname) {
        clientNickname = nickname;
    }

    public String getClientDescription() {
        return clientDescription;
    }

    public void setClientDescription(String description) {
        clientDescription = description;
    }

    public static int getClientTime(){
        return LocalDateTime.now().getSecond();
    }
}
