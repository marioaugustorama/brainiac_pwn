from singles.brainiac_singles_python import array_single
from stagers.brainiac_stagers_python import array_stagers
from stages.brainiac_stages_python import array_stages
from brainiac_libs.brainiac_cores.cores import Cores
from brainiac_libs.brainiac_debug.debug import Debug
class Gera_Payloads:
    def __init__(self,payload,LHost,LPort,encode=""):
        self.payload=payload
        self.LHost=LHost
        self.LPost=LPort
        self.encode=encode
    def list():
        for payload in array_stages:
            Cores.cores("vermelho","=> "+payload)
        for payload in array_stagers:
            Cores.cores("amarelo","=> "+payload)
        for payload in array_single:
            Cores.cores("azul","=> "+payload)


    def gera(payload,lhost,lport,encode=""):
        if payload in array_stages:
            if payload == "brainiac_stages_full":
                Debug.CRITICAL("[+] gerando payload [+]")
                Debug.INFO    ("nome => "+payload)
                Cores.cores("azul","[+]informacoes sobre o payload[+]")
                Cores.cores("verde","LHOST  => "+str(lhost))
                Cores.cores("verde","LPORT  => "+str(lport))
                if encode != None:
                    Cores.cores("verde","Encode => " + str(encode))

                else:
                    Cores.cores("verde","Encode[recomendo usar]")
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

















