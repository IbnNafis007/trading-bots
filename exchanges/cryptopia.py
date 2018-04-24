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
        # 1. Sender asks receiver for public key
        # 2. hash
        # 3. use private key to generate signature
        # 4. attach signature to message
        # 5. encryption of everything
        #'https://www.cryptopia.co.nz/api/GetBalance'
        '''
        url = 'https://www.cryptopia.co.nz/api/GetBalance'
        nonce = str(int(time.time()))
        #print(nonce)
        post_data = json.dumps(None)
        m = hashlib.md5()
        #m.encode('utf-8').hexdigest()
        #m.update(post_data)
        requestContentBase64String = base64.b64encode(m.digest())
        print(type(requestContentBase64String))
        signature = self.__apikey + 'POST' + url + nonce + str(requestContentBase64String)
        hmacsignature = base64.b64encode(str(hmac.new(base64.b64decode(self.__apisecret), signature, hashlib.sha256).digest(),'utf-8'))
        header_value = "amx " + self.__apikey + ":" + hmacsignature + ":" + nonce
        headers = {'Authorization': header_value, 'Content-Type': 'application/json; charset=utf-8'}
        r = requests.post(url, data=post_data, headers=headers) # data=post_data, headers '''
        req = {}
        #API_KEY + "POST" + URI + NONCE + HASHED_POST_PARAMS
        url = "https://www.cryptopia.co.nz/Api/GetBalance"
        nonce = str(int(time.time()))
        post_data = json.dumps(req)
        print("post_data: "+ post_data)
        m = hashlib.md5()
        #print("m: "+ str(m))
        m.update(bytes(post_data,'utf-8'))
        #m.update(post_data,'utf-8')
        requestContentBase64String = base64.b64encode(m.digest()).decode('utf-8')

        #print("requestContentBase64String: "+ requestContentBase64String)

        x = urllib.parse.quote_plus(url)#.lower()

        #print("[+] quote_plus: " + x)

        signature = self.__apikey + "POST" + url + nonce + requestContentBase64String

        print("[+] Signature: "+ signature)

        ascii_apisecret = self.__apisecret.encode('ascii','ignore')
        #print("[+] ASCII apisecret: "+ str(ascii_apisecret))

        decoded_apisecret = base64.b64decode(ascii_apisecret)
        #print("[+] decoded_apisecret: "+ str(decoded_apisecret))

        #myHMAC = hmac.new(decoded_apisecret, bytearray(signature,'utf8'), hashlib.sha256)
        myHMAC = hmac.new(bytes(self.__apisecret,'utf-8'), bytearray(signature,'utf-8'), hashlib.sha256)

        myDigest = myHMAC.digest()

        hmacsignature = base64.b64encode(myDigest)

        #print("[+] hmacsignature: " + str(hmacsignature))

        header_value = "amx " + self.__apikey + ":" + str(hmacsignature) + ":" + nonce

        #print("[+] header_value: "+ header_value)

        headers = {'Authorization': header_value, 'Content-Type': 'application/json; charset=utf-8'}

        response = requests.post(url, data=post_data, headers=headers).text
        #response = r.text
        #print('[+] Response' + response)
        #print(r)
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
    def filter_response(self, response):
        return response['Data']




    '''
        def getBalance(self):
        Returns all balances or a specific currency balance"""
        # 1. Sender asks receiver for public key
        # 2. hash
        # 3. use private key to generate signature
        # 4. attach signature to message
        # 5. encryption of everything
        #'https://www.cryptopia.co.nz/api/GetBalance'
        
        url = 'https://www.cryptopia.co.nz/api/GetBalance'
        nonce = str(int(time.time()))
        #print(nonce)
        post_data = json.dumps(None)
        m = hashlib.md5()
        #m.encode('utf-8').hexdigest()
        #m.update(post_data)
        requestContentBase64String = base64.b64encode(m.digest())
        print(type(requestContentBase64String))
        signature = self.__apikey + 'POST' + url + nonce + str(requestContentBase64String)
        hmacsignature = base64.b64encode(str(hmac.new(base64.b64decode(self.__apisecret), signature, hashlib.sha256).digest(),'utf-8'))
        header_value = "amx " + self.__apikey + ":" + hmacsignature + ":" + nonce
        headers = {'Authorization': header_value, 'Content-Type': 'application/json; charset=utf-8'}
        r = requests.post(url, data=post_data, headers=headers) # data=post_data, headers 
        req = {}
        #API_KEY + "POST" + URI + NONCE + HASHED_POST_PARAMS
        url = "https://www.cryptopia.co.nz/Api/GetBalance"
        nonce = str(int(time.time()))
        post_data = json.dumps(req)
        print("post_data: "+ post_data)
        m = hashlib.md5()
        #print("m: "+ str(m))
        m.update(bytes(post_data,'utf-8'))
        #m.update(post_data,'utf-8')
        requestContentBase64String = base64.b64encode(m.digest()).decode('utf-8')

        #print("requestContentBase64String: "+ requestContentBase64String)

        x = urllib.parse.quote_plus(url)#.lower()

        #print("[+] quote_plus: " + x)

        signature = self.__apikey + "POST" + url + nonce + requestContentBase64String

        print("[+] Signature: "+ signature)

        ascii_apisecret = self.__apisecret.encode('ascii','ignore')
        #print("[+] ASCII apisecret: "+ str(ascii_apisecret))

        decoded_apisecret = base64.b64decode(ascii_apisecret)
        #print("[+] decoded_apisecret: "+ str(decoded_apisecret))

        #myHMAC = hmac.new(decoded_apisecret, bytearray(signature,'utf8'), hashlib.sha256)
        myHMAC = hmac.new(bytes(self.__apisecret,'utf-8'), bytearray(signature,'utf-8'), hashlib.sha256)

        myDigest = myHMAC.digest()

        hmacsignature = base64.b64encode(myDigest)

        #print("[+] hmacsignature: " + str(hmacsignature))

        header_value = "amx " + self.__apikey + ":" + str(hmacsignature) + ":" + nonce

        #print("[+] header_value: "+ header_value)

        headers = {'Authorization': header_value, 'Content-Type': 'application/json; charset=utf-8'}

        response = requests.post(url, data=post_data, headers=headers).text
        #response = r.text
        #print('[+] Response' + response)
        #print(r)
        return response
'''