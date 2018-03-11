import itertools
import random
import binascii
import struct
import logging
import codecs
import hashlib
"""class com funcao de fazer o convert
     bytes para hex
     hex para bytes
     str para bytes
     bytes para str
     str para hex
     hex para str
     """
'''lib de auxiliacao
   ex:
       brainiac_utils.debug.INFO() # obtem informacoes sovre o processo
       brainiac_utils.debug.CRITICAL() #informacoes criticas
       brainiac_utils.debug.ERRO() # informacoes de erro
       brainiac_utils.debug.DEBUG() #debug da funcao
       brainiac_utils.debug.AVISO() #alertas
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
"""cp874	 	
cp875	 	
cp932	
cp949	
cp950	
cp1006	 	
cp1026	
cp1140	
cp1250	
cp1251	
cp1252	
cp1253	
cp1254	
cp1255	
cp1256	
cp1257	
cp1258	
euc_jp	
euc_jis_2004	
euc_jisx0213	
euc_kr	
gb2312	
gbk	
gb18030	
hz	
iso2022_jp	
iso2022_jp_1
iso2022_jp_2
iso2022_jp_2004
iso2022_jp_3	
iso2022_jp_ext	
iso2022_kr	
iso8859_2	
iso8859_3	
iso8859_4	
iso8859_5	
iso8859_6	
iso8859_7	
iso8859_8	
iso8859_9	
iso8859_10	
iso8859_11	
iso8859_13	
iso8859_14	
iso8859_15	
iso8859_16	
johab
koi8_r	 
koi8_u	 	
mac_cyrillic
mac_greek	
mac_iceland	
mac_latin2	
mac_roman	
mac_turkish	
ptcp154	
shift_jis	
shift_jis_2004	
shift_jisx0213	
utf_32	
utf_32_be	
utf_32_le	
utf_16	
utf_16_be	
utf_16_le	
utf_7	
utf_8	
utf_8_sig
idna	 	
mbcs	
palmos	 	
punycode	 	
raw_unicode_escape	 	
rot_13	
undefined
unicode_escape
unicode_internal
base64_codec
bz2_codec	
hex_codec	
quopri_codec	
string_escape	 	
zlib_codec"""
'''
        suporte ha 
        cp874	 	
cp875	 	
cp932	
cp949	
cp950	
cp1006	 	
cp1026	
cp1140	
cp1250	
cp1251	
cp1252	
cp1253	
cp1254	
cp1255	
cp1256	
cp1257	
cp1258	
euc_jp	
euc_jis_2004	
euc_jisx0213	
euc_kr	
gb2312	
gbk	
gb18030	
hz	
iso2022_jp	
iso2022_jp_1
iso2022_jp_2
iso2022_jp_2004
iso2022_jp_3	
iso2022_jp_ext	
iso2022_kr	
iso8859_2	
iso8859_3	
iso8859_4	
iso8859_5	
iso8859_6	
iso8859_7	
iso8859_8	
iso8859_9	
iso8859_10	
iso8859_11	
iso8859_13	
iso8859_14	
iso8859_15	
iso8859_16	
johab
koi8_r	 
koi8_u	 	
mac_cyrillic
mac_greek	
mac_iceland	
mac_latin2	
mac_roman	
mac_turkish	
ptcp154	
shift_jis	
shift_jis_2004	
shift_jisx0213	
utf_32	
utf_32_be	
utf_32_le	
utf_16	
utf_16_be	
utf_16_le	
utf_7	
utf_8	
utf_8_sig
idna	 	
mbcs	
palmos	 	
punycode	 	
raw_unicode_escape	 	
rot_13	
undefined
unicode_escape
unicode_internal
base64_codec
bz2_codec	
hex_codec	
quopri_codec	
string_escape	 	
zlib_codec
        '''