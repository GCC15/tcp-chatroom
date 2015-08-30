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
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class JavaChatRoomRegisterGUI extends JFrame {
    final JLabel labelServer = new JLabel("Server IP: ");
    final JLabel labelPort = new JLabel("Port: ");
    final JLabel labelID = new JLabel("New ID: ");
    final JLabel labelPassword = new JLabel("New Password: ");
    final JLabel labelConfirmPwd = new JLabel("Confirm Password: ");
    JLabel labelMessage = new JLabel("");
    final JTextField textFieldServer = new JTextField(20);
    final JTextField textFieldPort = new JTextField(20);
    final JTextField textFieldID = new JTextField(20);
    final JTextField textFieldPassword = new JTextField(20);
    final JTextField textFieldConfirmPwd = new JTextField(20);
    final JButton buttonSignUp = new JButton("Sign Up");

    public JavaChatRoomRegisterGUI() {
        super("Chatroom Sign Up");
        setResizable(false);
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));
        setSize(500, 250);
        JPanel panelServer = new JPanel();
        addComponentToPanel(panelServer, labelServer, textFieldServer);
        add(panelServer);
        JPanel panelPort = new JPanel();
        addComponentToPanel(panelPort, labelPort, textFieldPort);
        add(panelPort);
        JPanel panelID = new JPanel();
        addComponentToPanel(panelID, labelID, textFieldID);
        add(panelID);
        JPanel panelPassword = new JPanel();
        addComponentToPanel(panelPassword, labelPassword, textFieldPassword);
        add(panelPassword);
        JPanel panelConfirmPwd = new JPanel();
        addComponentToPanel(panelConfirmPwd, labelConfirmPwd, textFieldConfirmPwd);
        add(panelConfirmPwd);
        JPanel panelButton = new JPanel();
        panelButton.setLayout(new FlowLayout());
        buttonSignUp.addActionListener(new SignUpActionListener());
        panelButton.add(buttonSignUp);
        panelButton.add(labelMessage);
        add(panelButton);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        setVisible(true);
    }

    private void addComponentToPanel(JPanel panel, JLabel label,
                                     JTextField textField) {
        panel.setLayout(new FlowLayout());
        panel.add(label);
        panel.add(textField);
    }

    private boolean isServerIPValid() {
        String serverIP = textFieldServer.getText();
        if (true) {
            return true;
        } else {
            labelMessage.setText("Server IP is not valid");
            return false;
        }
    }

    private boolean isPortValid() {
        String Port = textFieldPort.getText();
        if (true) {
            return true;
        } else {
            labelMessage.setText("Port is not valid");
            return false;
        }
    }


    private boolean isIDUnique() {
        if (true) {
            return true;
        } else {
            labelMessage.setText("ID is not unique");
            return false;
        }
    }

    private boolean isIDValid() {
        String ID = textFieldID.getText();
        int length = ID.length();
        if (length < 1 || length > 16) {
            labelMessage.setText("ID length is not valid");
            return false;
        }
        for (int i = 0; i < length; i++) {
            if (!Character.isLetterOrDigit(ID.charAt(i))) {
                labelMessage.setText("ID contains invalid characters");
                return false;
            }
        }
        if (!isIDUnique()) {
            labelMessage.setText("ID is not unique");
            return false;
        }
        return true;
    }


    private boolean isPasswordValid() {
        String password = textFieldPassword.getText();
        int length = password.length();
        if (length < 6 || length > 64) {
            labelMessage.setText("Password length is not valid");
            return false;
        }
        for (int i = 0; i < length; i++) {
            if (!Character.isLetterOrDigit(password.charAt(i))) {
                labelMessage.setText("Password contains invalid characters");
                return false;
            }
        }
        return true;
    }

    private boolean isConfirmPwdValid() {
        String confirmPwd = textFieldConfirmPwd.getText();
        String password = textFieldPassword.getText();
        if (password.equals(confirmPwd)) {
            return true;
        } else {
            labelMessage.setText("Confirmed password is not identical to the password");
            return false;
        }
    }

    private class SignUpActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            isServerIPValid();
            isPortValid();
            isIDValid();
            isPasswordValid();
            isConfirmPwdValid();
        }
    }
}
