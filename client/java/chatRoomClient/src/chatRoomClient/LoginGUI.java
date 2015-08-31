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

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class LoginGUI extends JFrame {

    final JLabel labelServer = new JLabel("Server hostname: ");
    final JLabel labelPort = new JLabel("Port: ");
    final JLabel labelID = new JLabel("ID: ");
    final JLabel labelPassword = new JLabel("Password: ");
    final JTextField textFieldServer = new JTextField(20);
    final JTextField textFieldPort = new JTextField(20);
    final JTextField textFieldID = new JTextField(20);
    JPasswordField pwdFieldPassword = new JPasswordField(20);
    final JButton buttonLogIn = new JButton("Log In");
    final JButton buttonSignUp = new JButton("Sign Up");

    public LoginGUI() {
        super("Log In");
        setResizable(false);
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));
        setSize(400, 250);
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
        pwdFieldPassword.setEchoChar('*');
        addComponentToPanel(panelPassword, labelPassword, pwdFieldPassword);
        add(panelPassword);
        JPanel panelButton = new JPanel();
        panelButton.setLayout(new FlowLayout());
        buttonSignUp.addActionListener(new SignUpActionListener());
        panelButton.add(buttonSignUp);
        buttonLogIn.addActionListener(new LoginActionListener());
        panelButton.add(buttonLogIn);
        add(panelButton);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void addComponentToPanel(JPanel panel, JLabel label,
                                     JTextField textField) {
        panel.setLayout(new FlowLayout());
        panel.add(label);
        panel.add(textField);
    }


    private class SignUpActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            SwingUtilities.invokeLater(SignUpGUI::new);
        }
    }

    private class LoginActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                Validation.checkServer(textFieldServer.getText());
                Validation.checkPort(textFieldPort.getText());
                Validation.checkId(textFieldID.getText());
                Validation.checkPassword(new String(pwdFieldPassword.getPassword()));
            } catch (Validation.ValidationException exp) {
                Utils.showErrorDialog(exp.getMessage());
            }
            // TODO
        }
    }
}
