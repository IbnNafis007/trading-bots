from exchanges.exchange import Exchange
from env import coinbase

import requests

class Coinbase(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = coinbase['apikey']
        self.__apisecret = coinbase['apisecret']