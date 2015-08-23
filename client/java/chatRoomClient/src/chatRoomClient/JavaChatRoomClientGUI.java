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


public class JavaChatRoomClientGUI extends JFrame{
    JPanel panel1 = new JPanel();
    JPanel panel2 = new JPanel();
    JButton button1 = new JButton("Send");
    JTextArea textArea = new JTextArea(20,40);
    JTextField textField = new JTextField(40);

    public JavaChatRoomClientGUI() {
        super("Chat room client");
        setLayout(new BorderLayout());
        panel1.add(textArea);
        panel2.setLayout(new FlowLayout());
        panel2.add(textField);
        panel2.add(button1);
        add(panel1, BorderLayout.CENTER);
        add(panel2,BorderLayout.SOUTH);
        setSize(500, 500);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
	    SwingUtilities.invokeLater(JavaChatRoomClientGUI::new);
    }
}
