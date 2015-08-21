# Main controller of the relay server

import sys

import argparse

import server


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    # https://docs.python.org/3.5/howto/argparse.html

    # s = server.RelayServer()


if __name__ == '__main__':
    main()
