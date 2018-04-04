import logging
from brainiac_libs.brainiac_cores.cores import Cores
class Debug:
    """ex:brainiac_debug
            brainiac_utils.brainiac_debug.INFO() # obtem informações sobre o processo
            brainiac_utils.brainiac_debug.CRITICAL() #informações criticas
            brainiac_utils.brainiac_debug.ERRO() # informações de erro
            brainiac_utils.brainiac_debug.DEBUG() #brainiac_debug da função
            brainiac_utils.brainiac_debug.AVISO() #alertas
    """

    def __init__(self, DEBUG, INFO, AVISO, ERRO, CRITICAL):
        self.DEBUG = DEBUG
        self.INFO = INFO
        self.AVISO = AVISO
        self.ERRO = ERRO
        self.CRITICAL = CRITICAL

    def ERRO(self):
        Cores.cores("vermelho","Erro: "+self)

    def INFO(self):
        Cores.cores("amarelo", "INFO: "+self)

    def CRITICAL(self):
        Cores.cores("vermelho", "CRITICAL: "+self)

    def AVISO(self):
        Cores.cores("amarelo", "AVISO: "+self)

    def DEBUG(self):
        Cores.cores("azul", "DEBUG: "+self)

