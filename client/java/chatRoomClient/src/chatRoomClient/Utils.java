package chatRoomClient;

import javax.swing.*;

public final class Utils {
    private Utils() {

    }

    public static void showMessageDialog(String message) {
        // TODO: set title
        JOptionPane.showMessageDialog(new JFrame(), message);
    }
}
