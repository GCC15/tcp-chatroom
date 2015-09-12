# Copyright (C) 2015 Zhang NS, Zifan Li, Zichao Li
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import socket
import threading

import env


def serve():
    server_socket = socket.socket()
    server_socket.bind(('', env.get_server_port()))
    server_socket.listen(env.get_tcp_listen_backlog())
    while True:
        client_socket, address = server_socket.accept()
        # print('[Main] Connection established with {}'.format(address))
        cht = ClientHandlerThread(client_socket)
        print('[Main] Starting ClientHandlerThread {}'
              .format(cht.name))
        cht.start()


class ControlThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__control_socket = socket.socket()
        self.__control_port = env.get_control_port()

    def run(self):
        pass


class ClientHandlerThread(threading.Thread):
    """Handles a client"""

    def __init__(self, client_socket):
        super().__init__()
        self.__client_socket = client_socket

    def run(self):
        pass
