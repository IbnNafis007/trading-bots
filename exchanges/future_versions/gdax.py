from exchanges.exchange import Exchange
from env import gdax

import requests

class Gdax(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = gdax['apikey']
        self.__apisecret = gdax['apisecret']