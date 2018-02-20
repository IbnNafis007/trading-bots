from exchanges.exchange import Exchange
from env import bitstamp

import requests

class Bitstamp(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = bitstamp['apikey']
        self.__apisecret = bitstamp['apisecret']