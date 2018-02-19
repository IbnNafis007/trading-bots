from exchanges.exchange import Exchange
from env import hitbtc

import requests

class Hitbtc(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = hitbtc['apikey']
        self.__apisecret = hitbtc['apisecret']