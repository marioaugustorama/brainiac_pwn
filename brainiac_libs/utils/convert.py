import itertools
import random
import binascii
import struct
import logging
import codecs
import hashlib


class convert:
    def __init__(self):
        pass

    def str_para_bytes(self):
        print(self.encode())

    def bytes_para_str(self):
        print(str(self.decode("utf-8")))

    def str_para_hex(self):
        enc = binascii.hexlify(bytes(self, "UTF-8"))
        print(str(enc)[2:-1])

    def hex_para_str(self):
        print(bytes.fromhex(self).decode('utf-8'))

    def xor_bytes(b, key):
        if len(b) != len(key):
            brainiac_utils.debug.INFO("len(a) != len(b)")
        if len(b) > len(key):
            return brainiac_utils.convert.str_para_hex("".join([chr(x ^ y) for (x, y) in zip(b[:len(key)], key)]))
        else:
            return brainiac_utils.convert.str_para_hex("".join([chr(x ^ y) for (x, y) in zip(b, key[:len(b)])]))

    def xor_str(s, key):
        return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(s, itertools.cycle(key)))

    def xor_hexa(h, key):
        return brainiac_utils.convert.xor_bytes(brainiac_utils.convert.hex_para_str(h),
                                                brainiac_utils.convert.hex_para_str(key))
