#!/usr/bin/env python3
"""WHOIS protocol realization."""
import socket
from argparse import ArgumentParser


HOST = "whois.iana.org"
PORT = 43

def main():
    """WHOIS protocol realization."""
    addr, timeout = argument_parse()

    sock = socket.create_connection((HOST, PORT), timeout)
    sock.settimeout(timeout)

    try:
        sock.sendall("{}\r\n".format(addr).encode('utf-8'))
        while True:
            buff = sock.recv(4096)
            if not buff:
                break
            print(buff.decode('utf-8'), end='')
    finally:
        sock.close()
        print('Connection was closed')


def argument_parse():
    """Arguments parsing."""
    parser = ArgumentParser(prog='python whois.py', \
        description='WHOIS protocol realization', \
        epilog="(c) Semyon Makhaev, 2016. All rights reserved.")
    parser.add_argument('address', type=str, \
        help='IP-address for the request')
    parser.add_argument('timeout', type=int, default=180, \
        help='integer, the soconds count for the responce waiting. \
        The default value is 180', nargs='?')
    args = parser.parse_args()
    return args.address, args.timeout


if __name__ == "__main__":
    main()
