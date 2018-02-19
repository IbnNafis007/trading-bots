from exchanges.exchange import Exchange
from env import binance

import requests

class Binance(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = binance['apikey']
        self.__apisecret = binance['apisecret']

