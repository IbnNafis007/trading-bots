#/usr/bin/env python

import sys

sys.path.append('../../') # To keep file structure

from exchanges.cryptopia import Cryptopia

def main():
    exchange1 = Cryptopia()

    print(exchange1.getMarkets.__doc__)

main()