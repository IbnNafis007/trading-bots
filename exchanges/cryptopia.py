#/usr/bin/env python

from exchanges.exchange import Exchange
from env import cryptopia

import requests
import time

class Cryptopia(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = cryptopia['apikey']
        self.__apisecret = cryptopia['apisecret']

    # Public API
    def getCurrencies(self):
        """Returns all currency data."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetCurrencies')
        return (response.json())

    def getTradePairs(self):
        """Returns all trade pair data."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetTradePairs')
        return (response.json())

    def getMarkets(self, market=''):
        """Returns all market data."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarkets/' + market)
        return (response.json())

    def getMarket(self, market):
        """Returns market data for the specified trade pair."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarket/' + market)
        return (response.json())

    def getMarketHistory(self, market):
        """Returns the market history data for the specified trade pair."""
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarketHistory/' + market)
        return (response.json())

    def getMarketOrders(self):
        """Returns the open buy and sell orders for the specified trade pair."""
        pass

    def getMarketOrderGroups(self):
        """Returns the open buy and sell orders for the specified markets."""
        pass

    # Private API
    def getBalance(self):
        """Returns all balances or a specific currency balance"""
        response = requests.post('https://www.cryptopia.co.nz/api/GetBalance')
        pass

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