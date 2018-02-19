from exchanges.exchange import Exchange
from env import coinmarkets

import requests

class Coinmarkets(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = coinmarkets['apikey']
        self.__apisecret = coinmarkets['apisecret']