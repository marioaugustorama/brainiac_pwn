import itertools
import logging
from .cores import cores
class debug:
    """ex:debug
            brainiac_utils.debug.INFO() # obtem informacoes sovre o processo
            brainiac_utils.debug.CRITICAL() #informacoes criticas
            brainiac_utils.debug.ERRO() # informacoes de erro
            brainiac_utils.debug.DEBUG() #debug da funcao
            brainiac_utils.debug.AVISO() #alertas
    """

    def __init__(self, DEBUG, INFO, AVISO, ERRO, CRITICAL):
        self.DEBUG = DEBUG
        self.INFO = INFO
        self.AVISO = AVISO
        self.ERRO = ERRO
        self.CRITICAL = CRITICAL

    def ERRO(self):
        logging.error(cores.cores.verde + self)

    def INFO(self):
        logging.info(cores.cores.azul + self)

    def CRITICAL(self):
        logging.critical(cores.cores.azul + self)

    def AVISO(self):
        logging.warning(cores.cores.amarelo + self)

    def DEBUG(self):
        logging.debug(cores.cores.azul + self)
