# brainiac - CTF toolkit
![brainiac logo](https://raw.githubusercontent.com/darkcode357/brainiac_pwn/master/brainiac/brainiac-2.jpg?raw=true)

[![PyPI](https://img.shields.io/badge/pypi-v3.12.0-green.svg?style=flat)](https://pypi.python.org/pypi/pwntools/)
[![Travis](https://travis-ci.org/darkcode357/brainiac_pwn.svg)](https://travis-ci.org/darkcode357/brainiac_pwn)
[![Coveralls](https://img.shields.io/sonar/4.2/http/sonar.petalslink.com/org.ow2.petals%3Apetals-se-ase/tech_debt.svg)](https://coveralls.io/github/Gallopsled/pwntools?branch=dev)
[![Twitter](https://img.shields.io/badge/twitter-pwntools-4099FF.svg?style=flat)](https://twitter.com/pwntools)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

brainiac_pwn é uma biblioteca de desenvolvimento multi-plataforma , voltado para o desenvolvimento de ferramentas.

```python
from brainiac import * # importa todos os modulos
#importa um modulo especifico para poupar a memoria 
from brainiac_libs.brainiac_brute_force.services_bruteforce.bruteforce_smtp.brf_smtp import Smtp_brute
from brainiac_libs.brainiac_brute_force.services_bruteforce.bruteforce_ftp.brf_ftp import ftp_brute
from brainiac_libs.brainiac_brute_force.services_bruteforce.bruteforce_ssh.brf_ssh import Ssh_brute
#add smb_brute

from brainiac_libs.brainiac_debug.debug import Debug
from brainiac_libs.brainiac_cores.cores import Cores
#brainiac_services
from brainiac_libs.brainiac_hash_encode.hash_encode import Hash_encode
from brainiac_libs.brainiac_gera_wordlist.gera_wordlist import Gera_wordlist
from brainiac_libs.brainiac_encode.encode import Encode
from brainiac_libs.brainiac_decode.decode import Decode
from brainiac_libs.brainiac_convert.convert import Convert
from brainiac_libs.brainiac_baixar.baixar import Baixar
from brainiac_libs.brainiac_arquivo.arquivo import Arquivos
```

# Tente agora

Agora você pode fazer uma demonstração ao vivo do brainiac_pwn, [right in your browser](https://demo.pwntools.com).

# Documentação

Our documentation is available at [docs.pwntools.com](https://docs.pwntools.com/)

To get you started, we've provided some example solutions for past CTF challenges in our [write-ups repository](https://github.com/Gallopsled/pwntools-write-ups).

# instalação

O brainiac_pwn tem a maioria das funcionalidades deve funcionar em qualquer distribuição baseado em POSIX (Debian, Arch, FreeBSD, OSX, etc.). É necessário o Python 3.6.

A maior parte das funcionalidade do brainiac_pwn é autônoma e somente rodará com o python 3.6

O método de instalação conta com um auto detect que ira proceder as devidas configurações em sua máquina
atualmente suportada em distro bases(debian(deb)/ubuntu(deb)) base(arch-linux(pkg))

Temos 2 tipos de instalação:

1. Instalação pelo source:
    1. git clone https://github.com/darkcode357/brainiac_pwn
    2. cd brainiac_pwn
    3. python import brainiac  

2. Instalação via pip/ea3_install
    1. apt-get update
    2. apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
    3. easy_install3 brainiac_pwn
    4. pip3 install brainiac_pwn


No entanto, alguns dos recursos (assembling/disassembly foreign architectures) exigem dependências não-Python. Para mais informações, veja o #[complete installation instructions here](https://docs.pwntools.com/en/stable/install.html).


# Contribuição:
See [CONTRIBUTING.md](CONTRIBUTING.md)

# Erros
Se você tiver alguma dúvida por favor entre em contato através do [bug report](https://github.com/darkcode357/brainiac_pwn/issues)

# Canais de contato:
[facebook_page](https://www.facebook.com/brainiacpwntoolkit/) atualizações sobre a lib

[facebook_grupo](https://www.facebook.com/groups/1775847809390476/) debates/comunidade

[canal_irc](https://kiwiirc.com/client/irc.freenode.net/pwntools) debates/comunidade

[site futuramente](=) assim que eu pegar minha hospedagem

[forum futuramente](=) assim que eu pegar minha hospedagem
