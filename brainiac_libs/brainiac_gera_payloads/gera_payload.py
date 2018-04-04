from singles.brainiac_singles_python import array_single
from stagers.brainiac_stagers_python import array_stagers
from stages.brainiac_stages_python import array_stages
from brainiac_libs.brainiac_cores.cores import Cores
from brainiac_libs.brainiac_debug.debug import Debug


class GeraPayloads:
    def __init__(self,payload,lhost,lport,encode=""):
        self.payload=payload
        self.lhost=lhost
        self.lpost=lport
        self.encode=encode
    def list():
        for payload in array_stages:
            cores.cores("vermelho","=> " + payload)
        for payload in array_stagers:
            cores.cores("amarelo","=> " + payload)
        for payload in array_single:
            cores.cores("azul","=> " + payload)


    def gera(payload,lhost,lport,encode=""):
        if payload in array_stages:
            if payload == "brainiac_stages_full":
                debug.critical("[+] gerando payload [+]")
                debug.info    ("nome => " + payload)
                cores.cores("azul","[+]informações sobre o payload[+]")
                cores.cores("verde","lhost  => " + str(lhost))
                cores.cores("verde","lport  => " + str(lport))
                if encode != none:
                    cores.cores("verde","encode => " + str(encode))

                else:
                    cores.cores("verde","encode[recomendo usar]")
                def code():
                    with open("/tmp/brainiac_stages_full.py","w") as py:
                        dsa = """dsadsadsadsadsa
dasddsa"""
                        py.writelines("\n"+dsa+"\n")

                code()
        elif payload in array_stagers:
            print(payload)
        elif payload in array_single:
            print(payload)

















