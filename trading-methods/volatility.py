import sys
sys.path.append('../../') # To keep file structure

from exchanges.exchange import Exchange
from exchanges.cryptopia import Cryptopia

def main():
    exchange1 = Cryptopia()
    result = exchange1.getMarket('LTC_BTC')
    #print(result['Data'][0]['TradePairId'])
    #print(len(result['Data']))
    #print(result['Data'][497]['TradePairId'])
    #print(result)
    #for n in range(len(result['Data'])):
    #    print(result['Data'][n]['TradePairId'])

main()