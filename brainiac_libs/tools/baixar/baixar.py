import wget
from brainiac_libs.utils.debug import Debug
from brainiac_libs.utils.cores import Cores
import os


class Baixar():
    def __init__(self, url, arquivo, saida=""):
        self.url = url
        self.saida = saida
        self.arquivo = arquivo

    def baixar(url, saida=""):
        if url == None:
            print("[+]erro nao pode ser um argumento vazio")
            pass
        elif saida == None:
            print("local padrao [/tmp]")
            try:
                local = "/tmp"
                Debug.AVISO(local)
                arquivo = wget.download(url=url, out=local)
                print(Cores.amarelo + "=> " + Cores.verde + arquivo)
            except Exception:
                pass
        else:
            local = saida
            Debug.AVISO(local)
            arquivo = wget.download(url=url, out=local)
            print(Cores.amarelo + "=> " + Cores.verde + arquivo)

