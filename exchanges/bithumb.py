from exchanges.exchange import Exchange
from env import bithumb

import requests

class Bithumb(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = bithumb['apikey']
        self.__apisecret = bithumb['apisecret']