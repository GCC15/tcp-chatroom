from . import handler_thread


class Server:
    def __init__(self, port):
        self.port = port


class ClientHandler:
    def __init__(self, client_socket):
        ht = handler_thread.HandlerThread(client_socket)
