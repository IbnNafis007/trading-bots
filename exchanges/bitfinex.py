from exchanges.exchange import Exchange
from env import bitfinex

import requests

class Bitfinex(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = bitfinex['apikey']
        self.__apisecret = bitfinex['apisecret']