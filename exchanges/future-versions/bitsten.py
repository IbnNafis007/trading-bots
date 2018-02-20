from exchanges.exchange import Exchange
from env import bitsten

import requests

class Bitsten(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = bitsten['apikey']
        self.__apisecret = bitsten['apisecret']