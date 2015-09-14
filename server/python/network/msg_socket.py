"""Message-oriented socket wrapper"""

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

import env

import logger

MAX_BUFFER_SIZE = env.get_tcp_max_buffer_size()

LENGTH_PREFIX_SIZE = 4
LENGTH_LIMIT = 2 ** (8 * LENGTH_PREFIX_SIZE) - 1


def _int_to_bytes(n: int) -> bytes:
    return n.to_bytes(LENGTH_PREFIX_SIZE, 'big')


def _bytes_to_int(b: bytes) -> int:
    return int.from_bytes(LENGTH_PREFIX_SIZE, 'big')


class MessageSocket:
    """NOT thread-safe"""

    def __init__(self, sock):
        """
        :param sock: A socket-like object
        """
        self.__sock = sock

    def send_message(self, data: bytes):
        length = len(data)
        try:
            assert 1 <= length <= LENGTH_LIMIT
            self.__sock.sendall(_int_to_bytes(length) + data)
        except Exception as e:
            logger.e(str(e))
            raise SendMessageError()

    def receive_message(self) -> bytes:
        message_length = _bytes_to_int(self.__recv_all(LENGTH_PREFIX_SIZE))
        return self.__recv_all(message_length)

    def __recv_all(self, length: int) -> bytes:
        """Receive fixed length bytes"""
        chunks = []
        received_length = 0
        while received_length < length:
            chunk = self.__sock.recv(
                min(length - received_length, MAX_BUFFER_SIZE))
            if not chunk:
                # Connection has broken
                raise ReceiveMessageError()
            chunks.append(chunk)
            received_length += len(chunk)
        return b''.join(chunks)


class SendMessageError(IOError):
    """Error when sending a message"""


class ReceiveMessageError(IOError):
    """Error when receiving a message"""
