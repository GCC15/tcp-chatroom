// Helper methods for (a priori) input validations, and corresponding exceptions

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

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class Validation {

    private Validation() {
    }

    public static abstract class ValidationException extends Exception {
        public ValidationException(String message) {
            super(message);
        }
    }

    public static final class InvalidPortException extends ValidationException {
        public InvalidPortException() {
            super(Strings.INVALID_PORT);
        }
    }

    public static final class InvalidIdLengthException extends ValidationException {
        public InvalidIdLengthException() {
            super(Strings.INVALID_ID_LENGTH);
        }
    }

    public static final class InvalidIdCharException extends ValidationException {
        public InvalidIdCharException() {
            super(Strings.INVALID_ID_CHAR);
        }
    }

    public static final class InvalidPwdLengthException extends ValidationException {
        public InvalidPwdLengthException() {
            super(Strings.INVALID_PWD_LENGTH);
        }
    }

    public static final class InvalidPwdCharException extends ValidationException {
        public InvalidPwdCharException() {
            super(Strings.INVALID_PWD_CHAR);
        }
    }

    public static final class InvalidPwdConfirmException extends ValidationException {
        public InvalidPwdConfirmException() {
            super(Strings.INVALID_PWD_CONFIRM);
        }
    }

    public static void checkPort(String port) throws ValidationException {
        int portNum;
        try {
            portNum = Integer.parseInt(port);
        } catch (Exception e) {
            throw new InvalidPortException();
        }
        if (portNum < 1 || portNum > 65535) {
            throw new InvalidPortException();
        }
    }

    public static void checkId(String id) throws ValidationException {
        int length = id.length();
        if (length < 1 || length > 16) {
            throw new InvalidIdLengthException();
        }
        if (!id.matches("^[a-zA-Z0-9_]*$")){
            throw new InvalidIdCharException();
        }
    }


    public static void checkPassword(String password) throws ValidationException {
        int length = password.length();
        if (length < 6 || length > 64) {
            throw new InvalidPwdLengthException();
        }
        if (!password.matches("^[ -~]*$")){
            throw new InvalidPwdCharException();
        }
    }

    public static void checkPasswordConfirm(String password, String passwordConfirm) throws ValidationException {
        if (!password.equals(passwordConfirm)) {
            throw new InvalidPwdConfirmException();
        }
    }

}
