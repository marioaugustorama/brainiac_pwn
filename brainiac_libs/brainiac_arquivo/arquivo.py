from brainiac_libs.brainiac_debug.debug import Debug
from brainiac_libs.brainiac_cores.cores import *
from base64 import b64encode
from base64 import b32encode
from base64 import b16encode


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
            Debug.CRITICAL("brainiac_arquivo: " + arquivo)

            Debug.CRITICAL("escrita")
    def escrever_encode64(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b64encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.INFO("Arquivo: " + arquivo)

            Debug.CRITICAL("escrita " + decode)

    def escrever_encode32(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b32encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("Arquivo: " + arquivo)
            Debug.CRITICAL("escrita " + decode)
    def escrever_encode16(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b16encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("brainiac_arquivo: " + arquivo)
            Debug.CRITICAL("escrita " + decode)

