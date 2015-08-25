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


public class JavaChatRoomRegisterGUI extends JFrame {
    JLabel label1 = new JLabel("Server IP: ");
    JLabel label2 = new JLabel("Port: ");
    JLabel label3 = new JLabel("User ID: ");
    JLabel label4 = new JLabel("User Password: ");
    JTextField textField1 = new JTextField(20);
    JTextField textField2 = new JTextField(20);
    JTextField textField3 = new JTextField(20);
    JTextField textField4 = new JTextField(20);
    JButton button1 = new JButton("Register");

    public JavaChatRoomRegisterGUI() {
        super("Chat room register");
        setLayout(new FlowLayout(FlowLayout.LEFT, 20, 10));
        setSize(400, 250);
        add(label1);
        add(textField1);
        add(label2);
        add(textField2);
        add(label3);
        add(textField3);
        add(label4);
        add(textField4);
        add(button1);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);
    }
}
