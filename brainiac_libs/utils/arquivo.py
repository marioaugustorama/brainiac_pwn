from brainiac_libs.utils.debug import Debug
from brainiac_libs.utils.cores import Cores
from brainiac_libs.utils.encode import Encode
from base64 import b64encode
from base64 import b32encode
from base64 import b16encode
from base64 import b64decode
from base64 import b32decode
from base64 import b16decode

class Arquivos():
    def __init__(self,ler,escrever,tabulacao,encode):
        self.ler=ler
        self.escrever=escrever
        self.tabulacao=tabulacao
        self.encode=encode
    def ler(ler):
        with open(ler,"r") as ll:
            print(ll.read())
    def escrever(arquivo,escrever):
        with open(arquivo,"w") as ll:
            ll.write(escrever)
            Debug.CRITICAL("arquivo: "+arquivo)

            Debug.CRITICAL("escrita "+Cores.verde+escrever)
    def escrever_encode64(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b64encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("arquivo: "+arquivo)

            Debug.CRITICAL("escrita "+Cores.verde+decode)
    def escrever_encode32(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b32encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("arquivo: "+arquivo)

            Debug.CRITICAL("escrita "+Cores.verde+decode)
    def escrever_encode16(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b16encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("arquivo: "+arquivo)

            Debug.CRITICAL("escrita "+Cores.verde+decode)

Arquivos.escrever_encode16("/home/darkcode.txt","""dsa
darkcode
zerocode
""")