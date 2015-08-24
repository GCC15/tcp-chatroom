import socket
import time
import threading

import config as c


def main():
    for i in range(1):
        client_socket = socket.socket()
        # client_socket.connect(('localhost', c.get('server_port')))
        client_socket.connect(('52.74.148.102', c.get('server_port')))
        ct = ClientThread(client_socket)
        print('[Main] Starting ClientThread {}'.format(ct.getName()))
        ct.start()


class ClientThread(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.__s = client_socket

    def run(self):
        t0 = time.time()
        data = b's'*1000

        print('[{}] Length {}'.format(self.getName(), len(data)))
        print('[{}] Sent {}'.format(self.getName(), self.__s.send(data)))

        data = self.__s.recv(800)
        print('[{}] Received {}'.format(self.getName(), len(data)))

        data = self.__s.recv(800)
        print('[{}] Received {}'.format(self.getName(), len(data)))

        data = self.__s.recv(800)
        print('[{}] Received {}'.format(self.getName(), len(data)))

        self.__s.close()
        t1 = time.time()
        print('[{}] Time elapsed: {}'.format(self.getName(), t1 - t0))


if __name__ == '__main__':
    main()