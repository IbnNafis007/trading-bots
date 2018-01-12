import sys
sys.path.append('../../') # To keep file structure

from exchanges.coinexchange import Coinexchange

def main():
    exchange1 = Coinexchange()
    print(repr(exchange1.getMarkets.__doc__))
    result = exchange1.getMarkets()
    print(result)
    #result = exchange1.getMarket('LTC_BTC')
    #print(result['Data'][0]['TradePairId'])
    #print(len(result['Data']))
    #print(result['Data'][497]['TradePairId'])
    #print(result)
    #for n in range(len(result['Data'])):
    #    print(result['Data'][n]['TradePairId'])
main()