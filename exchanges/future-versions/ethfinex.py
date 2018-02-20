from exchanges.exchange import Exchange
from env import ethfinex

import requests

class Ethfinex(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = ethfinex['apikey']
        self.__apisecret = ethfinex['apisecret']