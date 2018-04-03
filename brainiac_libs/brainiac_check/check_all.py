import wget
import nmap
import itertools
import socket
class Check_all:
    def __init__(self,host,ports):
        self.host=host
        self.ports=ports

    def Check_All(host,ports):
