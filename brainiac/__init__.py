# coding=utf-8
from __future__ import absolute_import
import platform
import os
import subprocess
from brainiac_libs.brainiac_debug.debug import Debug
from brainiac_libs.brainiac_cores.cores import Cores
from .toplevel import *
import socket
import ipgetter
import sys
class check_brainiac:

    def ipi():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        a = s.getsockname()[0]
        Debug.INFO("[+]ip_interno " + a)

    def ipe():
        a = ipgetter.myip()
        Debug.INFO("[+]ip_interno "+a)
    def is_connected():
        try:
            socket.create_connection(("www.google.com", 80))
            Debug.INFO("[+]Brainiac_Online")
        except OSError:
            Debug.INFO("[+]Brainiac_off")

    def check_vm():
        pass

    def check_python_version():
        a = sys.version[0]
        b = sys.version[1]
        c = sys.version[2]
        t = a+b+c
        if t == "3.6":
            Debug.INFO("[+]python 3.6")
        else:
            exit(1)

    def check_gcc_version():
        gcc1 = platform.python_compiler()[4]
        gcc2 = platform.python_compiler()[5]
        gcc3 = platform.python_compiler()[6]
        gcc4 = platform.python_compiler()[7]
        gcc5 = platform.python_compiler()[8]
        version = str(gcc1 + gcc2 + gcc3 + gcc4 + gcc5)
        Debug.INFO("[+]gcc "+version)

    def check_id():
        if os.getuid() != 0:
            Debug.CRITICAL("[+]rode como root")
            Debug.CRITICAL("sudo python")
            Debug.CRITICAL("import brainiac")
            exit(1)

    def check_programas():
        list_cmd = ['msfconsole','john','johnny','iptables']
        for cmd in list_cmd:
            exist = subprocess.call('command -v ' + cmd + '>> /dev/null', shell=True)
            if exist == 0:
                pass
            else:
                print("efetue a instalacao do [%s]"%cmd)
                exit(1)
        Debug.INFO("[+]check programas =>[ok]")



if not platform.architecture()[0].startswith('64'):
    """Determina se o interpretador atual do Python é suportado pelo Brainiac"""
    Debug.CRITICAL("[+]Brainiac não suporta  o usod do Python 32 bits. Use uma versão de 64 bits.")
    exit(1)

else:
    check_brainiac.check_id()
    Cores.cores("vermelho","[+]brainiac importado")
    checkvm = Cores.cores("azul",input("ctf_local ou ctf_online ? [ctf_local/ctf_online] =>"))
    if checkvm == "ctf_local":
        check_brainiac.check_vm()
    elif checkvm == "ctf_online":
        check_brainiac.check_files_()
    else:
        print("[+]modo padrao ctf_online")
    Cores.cores("amarelo","[+]use help() para ter mais informacoes")
    Cores.cores("vermelho","###############################")
    Cores.cores("azul","[+]iniaciando checking")
    check_brainiac.is_connected()
    check_brainiac.ipe()
    check_brainiac.ipi()
    check_brainiac.check_python_version()
    check_brainiac.check_gcc_version()
    check_brainiac.check_programas()
