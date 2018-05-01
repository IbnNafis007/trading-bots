#/usr/bin/env python

from exchanges.exchange import Exchange
from env import cryptopia

import sys
import json
import requests
import time
import hmac
import urllib
import hashlib
import base64

class Cryptopia(Exchange):

    __apikey = ''
    __apisecret = ''
    __exchange = ''
    __minute_request_limit = 1000 # = 60000 #1000/minute
    __minimum_deposit = None
    __base_url = 'https://www.cryptopia.co.nz/api/'

    def __init__(self):
        self.__apikey = cryptopia['apikey']
        self.__apisecret = cryptopia['apisecret']
        self.__exchange = self.__class__.__name__

    # Public API
    def getCurrencies(self):
        """Returns all currency data."""
        response = self.api_call(requests.get('https://www.cryptopia.co.nz/api/GetCurrencies')) #self.api_call(requests.get(self.__base_url + '/GetCurrencies'))  #= requests.get('https://www.cryptopia.co.nz/api/GetCurrencies')
        return response
        #self.logRequest(self.__exchange)
        #with open('../../newfile.json','a') as f:
        #    json.dump(response.json(), f)
        #return self.checkResponse(response.json())

    def getTradePairs(self):
        """Returns all trade pair data."""
        response = requests.get('GetTradePairs')
        return response.json()

    def getMarkets(self, market=''):
        """Returns all market data."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarkets/' + market)
        return self.filter_response(response.json())

    def getMarket(self, market):
        """Returns market data for the specified trade pair."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarket/' + market)
        return response.json()

    def getMarketHistory(self, market):
        """Returns the market history data for the specified trade pair."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarketHistory/' + market)
        return response.json()

    def getMarketOrders(self, id):
        """Returns the open buy and sell orders for the specified trade pair."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarketOrders/' + id)

    def getMarketOrderGroups(self):
        """Returns the open buy and sell orders for the specified markets."""
        pass

    # Private API
    def getBalance(self):
        """Returns all balances or a specific currency balance"""
        request_parameters = {}
        url = self.__base_url + "getbalance"
        nonce = str(time.time())
        post_data = json.dumps(request_parameters)
        #m = hashlib.md5()
        #m.update(bytearray(post_data,'utf-8'))
        md5 = hashlib.md5()
        jsonparams = post_data.encode('utf-8')
        md5.update(jsonparams)
        rcb64 = base64.b64encode(md5.digest()).decode('utf-8')
        signature = self.__apikey + "POST" + urllib.parse.quote_plus(url).lower() + nonce + rcb64
        hmacsignature = base64.b64encode(hmac.new(base64.b64decode(self.__apisecret), signature.encode('utf-8'), hashlib.sha256).digest())
        header_value = "amx " + self.__apikey + ":" + hmacsignature.decode('utf-8') + ":" + nonce
        headers = {'Authorization': header_value, 'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url, data=post_data, headers=headers).text

        return response

    def getOpenOrders(self):
        pass

    def getDepositAddress(self):
        pass

    def getTradeHistory(self):
        pass

    def getTransactions(self):
        pass

    def submitTrade(self):
        pass

    def cancelTrade(self):
        pass

    def submitTip(self):
        pass

    def submitWithdraw(self):
        pass

    def submitTransfer(self):
        pass

    # Helper Methods
    def secure_headers(self, url, post_data):
        """ Creates secure header for cryptopia private api. """
        nonce = str(time.time())
        md5 = hashlib.md5()
        jsonparams = post_data.encode('utf-8')
        md5.update(jsonparams)
        rcb64 = base64.b64encode(md5.digest()).decode('utf-8')

        signature = self.key + "POST" + urllib.parse.quote_plus(url).lower() + nonce + rcb64
        hmacsignature = base64.b64encode(hmac.new(base64.b64decode(self.secret),
                                                  signature.encode('utf-8'),
                                                  hashlib.sha256).digest())
        header_value = "amx " + self.key + ":" + hmacsignature.decode('utf-8') + ":" + nonce
        return {'Authorization': header_value, 'Content-Type': 'application/json; charset=utf-8'}

    def filter_response(self, response):
        return response['Data']