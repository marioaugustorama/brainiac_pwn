import codecs
from brainiac_libs.brainiac_encode.conf_encode import *

class Encode:
    def encode(texto,ddencode):
        for k in arry_encode.values():
            if k == ddencode:
                enc = codecs.encode(texto,k)
                print(str(enc)[2:-1])

