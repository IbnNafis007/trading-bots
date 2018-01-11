from exchanges.exchange import Exchange
from env import kraken

import requests

class Kraken(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = kraken['apikey']
        self.__apisecret = kraken['apisecret']