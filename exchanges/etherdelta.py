from exchanges.exchange import Exchange
from env import etherdelta

import requests

class Etherdelta(Exchange):

    __apikey = ""
    __apisecret = ""

    def __init__(self):
        self.__apikey = etherdelta['apikey']
        self.__apisecret = etherdelta['apisecret']

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

    # Public API
    def getCurrencies(self):
        response = requests.get('https://www.cryptopia.co.nz/api/GetCurrencies')
        return(response.json())

    def getTradePairs(self):
        response = requests.get('https://www.cryptopia.co.nz/api/GetTradePairs')
        return(response.json())

    def getMarkets(self, market=0):
        if market == 0:
            response = requests.get('https://www.cryptopia.co.nz/api/GetMarkets')
        else:
            response = requests.get('https://www.cryptopia.co.nz/api/GetMarkets/'+market)
        return(response.json())

    def getMarket(self, market):
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarket/'+market)
        return(response.json())

    def getMarketHistory(self, market):
        response = requests.get('https://www.cryptopia.co.nz/api/GetMarketHistory/'+market)
        return(response.json())

    def getMarketOrders(self):
        pass

    def getMarketOrderGropus(self):
        pass

    




