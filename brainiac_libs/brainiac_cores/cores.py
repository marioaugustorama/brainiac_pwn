from brainiac_libs.brainiac_cores.conf_colors import *
#certinho by anon
class Cores:
    def cores(core,texto=""):
        """
        "vermelho"        :'\033[31m',

    "verde"           : '\033[32m',

    "azul"            :'\033[34m',

    "ciano"           : '\033[36m',

    "magenta"         : '\033[35m',

    "amarelo"         : '\033[33m',

    "preto "          : '\033[30m',

    "branco"          : '\033[37m',

    "normal"          : '\033[0;0m',

    "negrito"         : '\033[1m',

    "reverso "        : '\033[2m',

    "fundo_preto"     : '\033[40m',

    "fundo_vermelho"  : '\033[41m',

    "fundo_verde" :   '\033[42m',

    "fundo_amarelo"   : '\033[43m',

    "fundo_azul"      : '\033[44m',

    "fundo_magenta"   : '\033[45m',

    "fundo_ciano"     : '\033[46m',

    "fundo_branco"    :'\033[47m',


        :param core:
        :param texto:
        :return:
    """
        for k,v in arry_cores.items():
            if k == core:
                print(v+texto)



















