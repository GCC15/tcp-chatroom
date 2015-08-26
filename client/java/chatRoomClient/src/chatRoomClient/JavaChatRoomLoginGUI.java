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

public class JavaChatRoomLoginGUI extends JFrame {
<<<<<<< HEAD
    JLabel labelServer = new JLabel("Server IP: ");
    JLabel labelPort = new JLabel("Port: ");
    JLabel labelID = new JLabel("User ID: ");
    JLabel labelPassword = new JLabel("User Password: ");
    JTextField textFieldServer = new JTextField(20);
    JTextField textFieldPort = new JTextField(20);
    JTextField textFieldID = new JTextField(20);
    JTextField textFieldPassword = new JTextField(20);
    JButton button1 = new JButton("Login");
    JButton button2 = new JButton("Go to register page");
=======
    JLabel label1 = new JLabel("Server IP: ");
    JLabel label2 = new JLabel("Port: ");
    JLabel label3 = new JLabel("User ID: ");
    JLabel label4 = new JLabel("User Password: ");
    JTextField textField1 = new JTextField(20);
    JTextField textField2 = new JTextField(20);
    JTextField textField3 = new JTextField(20);
    JTextField textField4 = new JTextField(20);
    JButton button1 = new JButton("Log In");
    JButton button2 = new JButton("Sign Up");
>>>>>>> origin/master

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
        addComponentToPanel(panelID,labelID,textFieldID);
        add(panelID);
        JPanel panelPassword = new JPanel();
        addComponentToPanel(panelPassword,labelPassword,textFieldPassword);
        add(panelPassword);
        JPanel panelButton = new JPanel();
        panelButton.setLayout(new FlowLayout());
        panelButton.add(button1);
        button2.addActionListener(new RegisterActionListener());
        panelButton.add(button2);
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

    private static class RegisterActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            SwingUtilities.invokeLater(JavaChatRoomRegisterGUI::new);
        }
    }

}
