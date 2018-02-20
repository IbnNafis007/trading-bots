from exchanges.exchange import Exchange
from env import coinone

import requests

class Coinone(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = coinone['apikey']
        self.__apisecret = coinone['apisecret']