#by:darkcode0x00
from setuptools import setup, find_packages
from distutils.core import setup
from brainiac_libs.brainiac_cores.cores import Cores
from brainiac_libs.brainiac_debug.debug import Debug
import platform
from distutils.command.install import INSTALL_SCHEMES
from distutils.sysconfig import get_python_inc
from distutils.util import convert_path
import os
from os import getuid
if getuid() != 0:
    Debug.CRITICAL("rode como root")
    Debug.AVISO("sudo python setup.py install")
    exit(1)
dist = ["debian","ubuntu","arch"]#linux
for i in dist:
    if i == platform.dist()[0]:
        Cores.cores("vermelho","=> [%s]"%i)
PythonH = os.path.join(get_python_inc(), 'Python.h')
if not os.path.exists(PythonH):
    print(sys.stderr,"You must install the Python development headers!")
    print(sys.stderr,"$ apt-get install python-dev")
    sys.exit(-1)
setup(
  name = 'brainiac_pwn',
  packages=find_packages(),
  install_requires=[
        'beautifulsoup4',
        'requests',
        'filemagic',
        'passlib',
        'hexdump',
        'pymysql',
        'cx_Oracle',
        'psycopg2',
        'pymongo',
        'wget',
        'python-nmap',
        'GitPython',
        'nclib',
        'paramiko',
        'mako',
        'pyelftools',
        'capstone',
        'ropgadget',
        'pyserial',
        'requests',
        'pip',
        'tox',
        'rarfile',
        'pygments',
        'pysocks',
        'python-dateutil',
        'packaging',
        'psutil',
        'intervaltree',
        'unicorn',
        'pycurl',
        'ajpy',
        'pyopenssl',
        'cx_Oracle',
        'mysqlclient',
        'psycopg2',
        'pycrypto',
        'dnspython',
        'IPy',
        'pysnmp',
        'pyasn1',
        'pysmb'
    ],
  version = '3.7',
  description='lib voltada para o desenvolvimento de ferramentas para pentest',
  author='darkcode0x00',
  author_email='darkcode357@gmail.com',
  license='MIT',
  url = 'https://github.com/darkcode357/brainiac_pwn', # use the URL to the github repo
  download_url = 'https://raw.githubusercontent.com/darkcode357/brainiac_pwn/master/dist/brainiac_pwn-3.7-py3-none-any.whl', # I'll explain this in a second
)



#by:darkcode0x00
