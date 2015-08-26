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

import sun.reflect.generics.reflectiveObjects.NotImplementedException;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class JavaChatRoomLoginGUI extends JFrame {

    final JLabel labelServer = new JLabel("Server IP: ");
    final JLabel labelPort = new JLabel("Port: ");
    final JLabel labelID = new JLabel("User ID: ");
    final JLabel labelPassword = new JLabel("User Password: ");
    final JTextField textFieldServer = new JTextField(20);
    final JTextField textFieldPort = new JTextField(20);
    final JTextField textFieldID = new JTextField(20);
    final JTextField textFieldPassword = new JTextField(20);
    final JButton buttonLogin = new JButton("Log In");
    final JButton buttonSignup = new JButton("Sign Up");

    public JavaChatRoomLoginGUI() {
        super("Chat room log in");
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
        addComponentToPanel(panelPassword, labelPassword, textFieldPassword);
        add(panelPassword);
        JPanel panelButton = new JPanel();
        panelButton.setLayout(new FlowLayout());
        buttonSignup.addActionListener(new SignUpActionListener());
        panelButton.add(buttonSignup);
        buttonLogin.addActionListener(new LoginActionListener());
        panelButton.add(buttonLogin);
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

    private static class SignUpActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            SwingUtilities.invokeLater(JavaChatRoomRegisterGUI::new);
        }
    }

    private static class LoginActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            throw new NotImplementedException();
        }
    }

}
