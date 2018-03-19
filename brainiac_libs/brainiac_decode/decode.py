import codecs
from brainiac_libs.brainiac_decode.conf_decode import *
class Decode:
    def decode(texto,ddencode):
        for k in arry_decode.values():
            if k == ddencode:
                enc = codecs.encode(texto,k)
                print(str(enc)[2:-1])


