import logging
class Cores:
    '''lib cores
    ex:
        brainiac_utils.cores.$cor

            cyanClaro = "\033[1;36m"
            vermelho = '\033[31;1m'
            verde = '\033[32;1m'
            azul = '\033[34;1m'
            normal = '\033[0;0m'
            amarelo = '\033[1;33m'
            ciano = '\033[46m'
            magenta = '\033[45m'
            normal = '\033[0;0m'
    '''
    cyanClaro = "\033[1;36m"
    vermelho = '\033[31;1m'
    verde = '\033[32;1m'
    azul = '\033[34;1m'
    normal = '\033[0;0m'
    amarelo = '\033[1;33m'
    ciano = '\033[46m'
    magenta = '\033[45m'
    normal = '\033[0;0m'

class Debug:
    """ex:debug
            brainiac_utils.debug.INFO() # obtem informacoes sobre o processo
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
        logging.error(Cores.verde + self)

    def INFO(self):
        logging.info(Cores.azul + self)

    def CRITICAL(self):
        logging.critical(Cores.amarelo + self)

    def AVISO(self):
        logging.warning(Cores.amarelo + self)

    def DEBUG(self):
        logging.debug(Cores.amarelo + self)
