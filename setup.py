#by:darkcode0x00
from setuptools import setup, find_packages
from distutils.core import setup

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
        'nclib'
    ],
  version = '3.5',
  description='lib voltada para o desenvolvimento de ferramentas de pentest',
  author='darkcode0x00',
  author_email='darkcode357@gmail.com',
  license='MIT',
  url = 'https://github.com/darkcode357/brainiac_pwn', # use the URL to the github repo
  download_url = 'https://raw.githubusercontent.com/darkcode357/brainiac_pwn/master/dist/brainiac_pwn-3.5-py3-none-any.whl', # I'll explain this in a second
)
























#by:darkcode0x00
