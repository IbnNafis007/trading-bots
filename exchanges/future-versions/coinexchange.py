#/usr/bin/env python

from exchanges.exchange import Exchange
from env import coinexchange

import requests

class Coinexchange(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = coinexchange['apikey']
        self.__apisecret = coinexchange['apisecret']

    # Public API
    def getMarkets(self):
        """This endpoint retrieves all markets."""
        response = requests.get('https://www.coinexchange.io/api/v1/getmarkets')
        return (response.json())

    def getMarketSummaries(self):
        """This endpoint retrieves summaries for all markets."""
        response = requests.get('https://www.coinexchange.io/api/v1/getmarketsummaries')
        return (response.json())

    def getMarketSummary(self, market_id):
        """This endpoint retrieves summary for the specified market."""
        response = requests.get('https://www.coinexchange.io/api/v1/getmarketsummary?market_id=' + market_id)
        return (response.json())

    def getOrderBook(self, market_id):
        """This endpoint retrieves the top 50 buy and sell order for the market."""
        response = requests.get('https://www.coinexchange.io/api/v1/getorderbook?market_id=' + market_id)
        return (response.json())

    def getCurrencies(self):
        """This endpoint retrieves all enabled currencies / assets."""
        response = requests.get('https://www.coinexchange.io/api/v1/getcurrencies')
        return (response.json())

    def getCurrency(self, currency_id):
        """This endpoint retrieves information about a single currency / asset."""
        response = requests.get('https://www.coinexchange.io/api/v1/getcurrency?currency_id=' + currency_id)
        return (response.json())

    # Private API