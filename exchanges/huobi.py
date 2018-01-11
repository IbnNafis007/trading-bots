from exchanges.exchange import Exchange
from env import huobi

import requests

class Huobi(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = huobi['apikey']
        self.__apisecret = huobi['apisecret']