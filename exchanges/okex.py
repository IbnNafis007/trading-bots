from exchanges.exchange import Exchange
from env import okex

import requests

class Okex(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = okex['apikey']
        self.__apisecret = okex['apisecret']