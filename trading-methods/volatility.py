import sys
sys.path.append('../') # To keep file structure

from exchanges.exchange import Exchange
from exchanges.cryptopia import Cryptopia

def main():
    exchange1 = Cryptopia()
    #exchange1.getapikey()
    #cryptopiaExchange.getTemp()
    #print(cryptopia)

main()