from exchanges.exchange import Exchange
from env import livecoin

import requests

class Livecoin(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = livecoin['apikey']
        self.__apisecret = livecoin['apisecret']