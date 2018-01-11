from exchanges.exchange import Exchange
from env import yobit

import requests

class Yobit(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = yobit['apikey']
        self.__apisecret = yobit['apisecret']