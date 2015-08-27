import threading


class HandlerThread(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.__s = client_socket

    def run(self):
        pass
