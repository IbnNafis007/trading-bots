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
        response = requests.get('https://www.coinexchange.io/api/v1/getmarketsummaries')
        return (response.json())

    def getMarkets(self, market=0):
        if market == 0:
            response = requests.get('https://www.cryptopia.co.nz/api/GetMarkets')
        else:
            response = requests.get('https://www.cryptopia.co.nz/api/GetMarkets/' + market)
        return (response.json())

    def getMarket(self, market):
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarket/' + market)
        return (response.json())

    def getMarketHistory(self, market):
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarketHistory/' + market)
        return (response.json())

    def getMarketOrders(self):
        pass

    def getMarketOrderGropus(self):
        pass

    # Private API
    def getBalance(self):
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