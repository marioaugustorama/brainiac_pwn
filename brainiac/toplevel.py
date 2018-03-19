import brainiac_libs
from brainiac_libs.brainiac_arquivo import arquivo
from brainiac_libs.brainiac_baixar import baixar
from brainiac_libs.brainiac_cores.cores import Cores
from brainiac_libs.brainiac_convert.convert import Convert
from brainiac_libs.brainiac_debug.debug import Debug
from brainiac_libs.brainiac_decode.decode import Decode
from brainiac_libs.brainiac_encode.encode import  Encode
from brainiac_libs.brainiac_gera_wordlist.gera_wordlist import Gera_wordlist
from brainiac_libs.brainiac_hash_encode.hash_encode import Hash_encode






try:
    import cPickle as pickle
except ImportError:
    import pickle
