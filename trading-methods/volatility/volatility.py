#/usr/bin/env python

import os
import sys
import json
import time

#sys.path.append('../../') # To keep file structure
sys.path += '../../'

from exchanges.cryptopia import Cryptopia

def main():
    #print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #print(sys.path)
    cryptopia = Cryptopia()
    #print(cryptopia.getCurrencies())

    #start = time.time()
    #prices = dict()


    print(cryptopia.getBalance())
    #print(cryptopia.test())

    #post is

'''
    for i in range(len(prices)):
                                ''
        #Check if price is 1 or 2 sats
        if .00000001 <= prices[i]['BidPrice'] <= .00000002:
            print(prices[i]['BidPrice'])
      '''


    #print(prices)
    #print(type(prices))
    #print(type(prices))

    #cryptopia.filterResponse(prices)

    #print(time.time() - start)

    #print(cryptopia.getMarkets.__doc__)

main()