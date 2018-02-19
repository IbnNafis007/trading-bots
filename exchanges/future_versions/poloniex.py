from exchanges.exchange import Exchange
from env import poloniex

import requests

class Poloniex(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = poloniex['apikey']
        self.__apisecret = poloniex['apisecret']