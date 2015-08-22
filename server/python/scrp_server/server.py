import socket
from . import db_adapter


class Server:
    def __init__(self, port):
        self.port = port
