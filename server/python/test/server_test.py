import socket
import threading
import time
import random

import env


def main():
    server_socket = socket.socket()
    server_socket.bind(('', env.get_server_port))
    server_socket.listen(env.get_tcp_listen_backlog)
    while True:
        print('[Main] Waiting for a new connection request...')
        client_socket, address = server_socket.accept()
        print('[Main] Connection established with {}'.format(address))
        cht = ClientHandlerThread(client_socket)
        print('[Main] Starting ClientHandlerThread {}'
              .format(cht.name))
        cht.start()


class ClientHandlerThread(threading.Thread):
    """A thread to handle one client"""

    def __init__(self, client_socket):
        super().__init__()
        self.__s = client_socket
        self.__recv_buffersize = 32767
        self.__k = 2

    def run(self):
        data = self.__s.recv(self.__recv_buffersize)
        print('[{}] Received {}'.format(self.name, len(data)))
        time.sleep(random.random() * 5)
        print('[{}] Sent {}'.format(
            self.name, self.__s.send(data * self.__k))
        )
        print('[{}] Sent {}'.format(
            self.name, self.__s.send(data * self.__k))
        )
        self.__s.close()


if __name__ == '__main__':
    main()
