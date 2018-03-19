import itertools
import binascii
from brainiac_libs.brainiac_debug.debug import Debug
class Convert:
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
            Debug.INFO("len(a) != len(b)")
        if len(b) > len(key):
            return Convert.str_para_hex("".join([chr(x ^ y) for (x, y) in zip(b[:len(key)], key)]))
        else:
            return Convert.str_para_hex("".join([chr(x ^ y) for (x, y) in zip(b, key[:len(b)])]))

    def xor_str(s, key):
        return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(s, itertools.cycle(key)))

    def xor_hexa(h, key):
        return Convert.xor_bytes(Convert.hex_para_str(h),Convert.hex_para_str(key))
