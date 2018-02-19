from exchanges.exchange import Exchange
from env import gemini

import requests

class Gemini(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = gemini['apikey']
        self.__apisecret = gemini['apisecret']