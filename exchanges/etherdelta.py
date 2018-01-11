from exchanges.exchange import Exchange
from env import etherdelta

import requests

class Etherdelta(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = etherdelta['apikey']
        self.__apisecret = etherdelta['apisecret']