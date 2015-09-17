"""
Socket wrapper classes for layered abstractions.

socket
BytesMessageSocketWrapper
UnicodeSocketWrapper
JsonSocketWrapper
"""

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

import json

import env
import logger


class SendBytesMessageError(IOError):
    """Fatal error when trying to send a bytes message"""


class ReceiveBytesMessageError(IOError):
    """Fatal error when trying to receive a bytes message"""


class BytesMessageSocketWrapper:
    """
    Bytes-message-oriented socket wrapper.
    NOT thread-safe.
    """

    # Maximum buffer size of TCP receive
    MAX_BUFFER_SIZE = env.get_tcp_max_buffer_size()

    # Length of the message length prefix, in bytes
    LENGTH_PREFIX_SIZE = 4
    LENGTH_LIMIT = 2 ** (8 * LENGTH_PREFIX_SIZE) - 1

    def __init__(self, sock):
        """
        :param sock: A connected socket-like object
        """
        self.__sock = sock

    def send_bytes(self, message: bytes):
        """
        Send a bytes message.
        Raise SendBytesMessageError if connection is broken.
        """
        length = len(message)
        assert 1 <= length <= BytesMessageSocketWrapper.LENGTH_LIMIT
        try:
            self.__sock.sendall(self._int_to_bytes(length) + message)
        except Exception as e:
            # Connection is broken
            logger.e(str(e))
            raise SendBytesMessageError()

    def receive_bytes(self) -> bytes:
        """
        Receive a bytes message.
        Raise ReceiveBytesMessageError if connection is broken.
        """
        message_length = self._bytes_to_int(
            self.__recv_all(BytesMessageSocketWrapper.LENGTH_PREFIX_SIZE))
        return self.__recv_all(message_length)

    def __recv_all(self, length: int) -> bytes:
        """
        Receive bytes of given length.
        Raise ReceiveBytesMessageError if connection is broken.
        """
        assert 1 <= length <= BytesMessageSocketWrapper.LENGTH_LIMIT
        chunks = []
        received_length = 0
        while received_length < length:
            chunk = self.__sock.recv(
                min(
                    length - received_length,
                    BytesMessageSocketWrapper.MAX_BUFFER_SIZE
                )
            )
            if not chunk:
                # Connection is broken
                raise ReceiveBytesMessageError()
            chunks.append(chunk)
            received_length += len(chunk)
        return b''.join(chunks)

    @staticmethod
    def _int_to_bytes(n: int) -> bytes:
        return n.to_bytes(BytesMessageSocketWrapper.LENGTH_PREFIX_SIZE, 'big')

    @staticmethod
    def _bytes_to_int(b: bytes) -> int:
        return int.from_bytes(b, 'big')


class UnicodeSocketWrapper:
    """
    Unicode-message-oriented socket wrapper.
    NOT thread-safe.
    """

    def __init__(self, bytes_msg_sock: BytesMessageSocketWrapper):
        self.__bytes_msg_sock = bytes_msg_sock

    def send_str(self, string: str):
        """Send a string message"""
        self.__bytes_msg_sock.send_bytes(string.encode())

    def receive_str(self) -> str:
        """
        Receive a string message.
        Raise UnicodeDecodeError if decoding failed.
        """
        return self.__bytes_msg_sock.receive_bytes().decode()


class JsonParseError(ValueError):
    """Error when parsing JSON to Python dict"""


class JsonSocketWrapper:
    """
    JSON-object-oriented socket wrapper.
    NOT thread-safe.
    """

    def __init__(self, unicode_sock: UnicodeSocketWrapper):
        self.__unicode_sock = unicode_sock

    def send_json(self, obj: dict):
        assert type(obj) == dict
        string = json.dumps(obj, separators=(',', ':'))
        self.__unicode_sock.send_str(string)

    def receive_json(self) -> dict:
        string = self.__unicode_sock.receive_str()
        try:
            obj = json.loads(string)
        except Exception as e:
            logger.e(str(e))
            raise JsonParseError()
        if type(obj) != dict:
            raise JsonParseError()
