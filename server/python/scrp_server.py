"""SCRP server core"""

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
import logger


class ServerThread(threading.Thread):
    """Main Daemon thread"""

    def __init__(self):
        super().__init__(name='ServerThread')
        self.__ct = ControlThread(self)
        # Store all ClientHandlerThreads
        self.__cht_set = set()
        # Map user_id -> cht
        self.__id_cht_dict = {}
        # Synchronize
        self.lock = threading.RLock()

    def cht_ready(self, cht: 'ClientHandlerThread'):
        """Inform that a cht is ready"""
        with self.lock:
            logger.d(str(cht))
            self.__cht_set.add(cht)

    def run(self):
        logger.i('ServerThread started')
        # Start the control thread
        self.__ct.start()
        # Start listening
        server_socket = socket.socket()
        server_port = env.get_server_port()
        server_socket.bind(('', server_port))
        server_socket.listen(env.get_tcp_listen_backlog())
        logger.i('Listening on server port {}'.format(server_port))
        while True:
            logger.i('Waiting for a new client connection')
            client_socket, address = server_socket.accept()
            logger.i('Connection established with client {}'.format(address))
            cht = ClientHandlerThread(self, client_socket)
            logger.i('Starting ClientHandlerThread {}'.format(cht.name))
            cht.start()


class ControlThread(threading.Thread):
    """
    Receive control messages from controllers (scrpd.py)
    """

    def __init__(self, server_thread: ServerThread):
        super().__init__(name='ControlThread')
        self.__st = server_thread

    def run(self):
        logger.i('ControlThread started')
        control_socket = socket.socket()
        control_port = env.get_control_port()
        # Only allow control messages from localhost for security
        control_socket.bind(('localhost', control_port))
        control_socket.listen(env.get_tcp_listen_backlog())
        logger.i('Listening on control port {}'.format(control_port))
        while True:
            logger.i('Waiting for a new controller connection')
            client_socket, address = control_socket.accept()
            logger.i('Connection established with controller {}'
                     .format(address))
            # TODO


class ClientHandlerThread(threading.Thread):
    """Handles a client"""

    def __init__(self, st: ServerThread, client_socket: socket.socket):
        super().__init__()
        self.__st = st
        self.__client_socket = client_socket

    def run(self):
        logger.i('ClientHandlerThread {} started'.format(self.name))
        self.__st.cht_ready(self)

