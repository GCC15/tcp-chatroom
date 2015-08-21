# Main controller of the chatroom server

import sys

import argparse

import server


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    # https://docs.python.org/3.5/howto/argparse.html

    # s = server.ChatroomServer()


if __name__ == '__main__':
    main()
