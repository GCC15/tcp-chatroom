"""Threads to be used by the SCRP server"""

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

from database.dao import Dao
from scrp.request import ScrpRequest, InvalidRequestDictError
from scrp.push import ScrpPush
from scrp.error import *
from network.sockets import *
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
        self.__lock = threading.RLock()

    def cht_ready(self, cht: 'ClientHandlerThread'):
        """Inform that a cht is ready"""
        with self.__lock:
            logger.d(str(cht))
            self.__cht_set.add(cht)

    def run(self):
        logger.i('I started')
        # Start the control thread
        self.__ct.start()
        # Start listening
        server_sock = socket.socket()
        server_port = env.get_server_port()
        server_sock.bind(('', server_port))
        server_sock.listen(env.get_tcp_listen_backlog())
        logger.i('Listening on server port {}'.format(server_port))
        while True:
            logger.i('Waiting for a new client connection')
            client_sock, address = server_sock.accept()
            logger.i('Connection established with client {}'.format(address))
            cht = ClientHandlerThread(self, client_sock)
            logger.i('Starting ClientHandlerThread {}'.format(cht.name))
            cht.start()


class ControlThread(threading.Thread):
    """
    Receive control messages from controllers (scrpd.py)
    """

    def __init__(self, st: ServerThread):
        super().__init__(name='ControlThread')
        self.__st = st

    def run(self):
        logger.i('I started')
        control_sock = socket.socket()
        control_port = env.get_control_port()
        # Only allow control messages from localhost for security
        control_sock.bind(('localhost', control_port))
        control_sock.listen(env.get_tcp_listen_backlog())
        logger.i('Listening on control port {}'.format(control_port))
        while True:
            logger.i('Waiting for a new controller connection')
            client_sock, address = control_sock.accept()
            logger.i('Connection established with controller {}'
                     .format(address))
            # TODO


class ClientHandlerThread(threading.Thread):
    """Handle a client"""

    def __init__(self, st: ServerThread, client_sock: socket.socket):
        super().__init__()
        self.__st = st
        self.__client_sock = client_sock
        self.__bytes_msg_sock = BytesMessageSocketWrapper(self.__client_sock)
        self.__unicode_sock = UnicodeSocketWrapper(self.__bytes_msg_sock)
        self.__json_sock = JsonSocketWrapper(self.__unicode_sock)
        self.__scrp_sock = ScrpSocketWrapper(self.__json_sock)
        self.__lock = threading.RLock()

    def run(self):
        logger.i('I started')
        self.__st.cht_ready(self)
        while True:
            try:
                request = self.__scrp_sock.receive_request()
                rht = RequestHandlerThread(self, request)
                rht.start()
            except BytesMessageReceiveError as e:
                # Connection is broken
                break
            except (MessageDecodeError,
                    JsonParseError,
                    InvalidRequestDictError) as e:
                # Bad request
                raise BadRequestError
            except ScrpError as e:
                logger.d(str(e))
        logger.d("Thread terminate")

    def send_response(self, response: ScrpResponse):
        with self.__lock:
            pass

    def send_push(self, push: ScrpPush):
        with self.__lock:
            pass


class RequestHandlerThread(threading.Thread):
    """Handle a given request"""

    def __init__(self, cht: ClientHandlerThread, request: ScrpRequest):
        super().__init__()
        self.__cht = cht
        self.__req = request
        self.__dao = Dao()

    def run(self):
        logger.i('I started')

