from exchanges.exchange import Exchange
from env import cryptopia

class Cryptopia(Exchange):

    __apikey = ""

    def __init__(self):
        print("initialized")
        self.__apikey = cryptopia['apikey']

