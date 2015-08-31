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

package chatRoomClient;

import javax.swing.*;

public class JavaValidation {
    public static void createDialog(String message){
        JOptionPane.showMessageDialog(new JFrame(),message);
    }
    public static boolean isServerIPValid(String serverIP) {
        if (true) {
            return true;
        } else {
            createDialog("Server IP is not valid");
            return false;
        }
    }

    public static boolean isPortValid(String port) {
        if (true) {
            return true;
        } else {
            createDialog("Port is not valid");
            return false;
        }
    }

    private static boolean isIDUnique(String ID) {
        if (true) {
            return true;
        } else {
            createDialog("ID is not unique");
            return false;
        }
    }

    public static boolean isIDValid(String ID) {
        int length = ID.length();
        if (length < 1 || length > 16) {
            createDialog("ID length is not valid, should be 1~16");
            return false;
        }
        for (int i = 0; i < length; i++) {
            if (!Character.isLetterOrDigit(ID.charAt(i))) {
                createDialog("ID contains invalid characters");
                return false;
            }
        }
        if (!isIDUnique(ID)) {
            createDialog("ID is not unique");
            return false;
        }
        return true;
    }


    public static boolean isPasswordValid(String password) {
        int length = password.length();
        if (length < 6 || length > 64) {
            createDialog("Password length is not valid, should be 6~64");
            return false;
        }
        for (int i = 0; i < length; i++) {
            if (!Character.isLetterOrDigit(password.charAt(i))) {
                createDialog("Password contains invalid characters");
                return false;
            }
        }
        return true;
    }

    public static boolean isConfirmPwdValid(String confirmPwd, String password) {
        if (password.equals(confirmPwd)) {
            return true;
        } else {
            createDialog("Confirmed password is not identical to the password");
            return false;
        }
    }

    public static boolean doesIDPwdMatch(String ID, String password){
        if (true) {
            return true;
        }
        else{
            return false;
        }
    }

}
