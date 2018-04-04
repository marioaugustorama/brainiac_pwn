import wget
from brainiac_libs.brainiac_debug.debug import Debug
from brainiac_libs.brainiac_cores.cores import Cores
import os


class Baixar():
    def __init__(self, url, arquivo, saida=""):
        self.url = url
        self.saida = saida
        self.arquivo = arquivo

    def baixar(url, saida=""):
        if url == None:
            print("[+]erro não pode ser um argumento vazio")
            pass
        elif saida == None:
            print("local padrão [/tmp]")
            try:
                local = "/tmp"
                arquivo = wget.download(url=url, out=local)
                Debug.AVISO("Diretório => [" + local + "]")
                Debug.AVISO("Arquivo => [" + arquivo + "]")
            except Exception:
                pass
        else:
            local = saida
            arquivo = wget.download(url=url, out=local)
            Debug.AVISO("Diretório => ["+local+"]")
            Debug.AVISO("Arquivo => ["+arquivo+"]")
