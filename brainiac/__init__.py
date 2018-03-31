from __future__ import absolute_import
import platform
from brainiac_libs.brainiac_debug.debug import Debug
from brainiac_libs.brainiac_cores.cores import Cores
from .toplevel import *



if not platform.architecture()[0].startswith('64'):
    """Determina se o interpretador atual do Python é suportado pelo Brainiac"""
    Debug.CRITICAL("Brainiac não suporta  o usod do Python 32 bits. Use uma versão de 64 bits.")
    exit(1)
else:
    Cores.cores("azul","check[ok]")
    Cores.cores("vermelho","brainiac importado[+]")
    Cores.cores("amarelo","use help() para ter mais informacoes[+]")
    Cores.cores("normal"," ")
