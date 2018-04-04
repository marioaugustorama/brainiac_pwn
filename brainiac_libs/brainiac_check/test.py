#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import socket

NUM_CORES = 8


def ping(host, port):
    try:
        socket.socket().connect((host, port))
        print(str(port) + " Open")
        return port
    except socket.error as err:
        if err.errno == ECONNREFUSED:
            return False
        raise


def scan_ports(host):
    p = Pool(NUM_CORES)
    ping_host = partial(ping, host)
    return filter(bool, p.map(ping_host, range(1, 65536)))


def main(host=None):
    if host is None:
        host = "127.0.0.1"

    print("\nScanning ports on " + host + " ...")
    ports = list(scan_ports(host))
    print("\nDone.")

    print(str(len(ports)) + " ports available.")
    print(ports)


if __name__ == "__main__":
    main("google.com")
