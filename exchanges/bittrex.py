from exchanges.exchange import Exchange
from env import bittrex

import requests

class Bittrex(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = bittrex['apikey']
        self.__apisecret = bittrex['apisecret']