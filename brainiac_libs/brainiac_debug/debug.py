import logging
from brainiac_libs.brainiac_cores.cores import *

class Debug:
    """ex:brainiac_debug
            brainiac_utils.brainiac_debug.INFO() # obtem informacoes sobre o processo
            brainiac_utils.brainiac_debug.CRITICAL() #informacoes criticas
            brainiac_utils.brainiac_debug.ERRO() # informacoes de erro
            brainiac_utils.brainiac_debug.DEBUG() #brainiac_debug da funcao
            brainiac_utils.brainiac_debug.AVISO() #alertas
    """

    def __init__(self, DEBUG, INFO, AVISO, ERRO, CRITICAL):
        self.DEBUG = DEBUG
        self.INFO = INFO
        self.AVISO = AVISO
        self.ERRO = ERRO
        self.CRITICAL = CRITICAL

    def ERRO(self):
        cores("vermelho","Erro: "+self)

    def INFO(self):
        cores("amarelo", "INFO: "+self)

    def CRITICAL(self):
        cores("vermelho", "CRITICAL: "+self)

    def AVISO(self):
        cores("ciano", "AVISO: "+self)

    def DEBUG(self):
        cores("azul", "DEBUG: "+self)

