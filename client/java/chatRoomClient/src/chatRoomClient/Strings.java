// Define all string constants in UI here.
// TODO: Consider moving to text files for internationalization, e.g. *.properties.

package chatRoomClient;

public final class Strings {

    private Strings() {
    }
    public static final String INVALID_SERVER = "Server is not valid";

    public static final String INVALID_PORT = "Port is not valid";

    public static final String INVALID_ID_LENGTH = "ID length is not valid, should be 1~16";

    public static final String INVALID_ID_CHAR = "ID contains invalid characters";

    public static final String INVALID_PWD_LENGTH = "Password length is not valid, should be 6~64";

    public static final String INVALID_PWD_CHAR = "Password contains invalid characters";

    public static final String INVALID_PWD_CONFIRM = "Confirmed password is not identical to the password";
}
