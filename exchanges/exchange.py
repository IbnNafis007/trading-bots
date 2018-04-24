#/usr/bin/env python

import sys
import json
import requests

# Parent Class for Exchanges
class Exchange(object):

    def __init__(self):
        pass

    def api_call(self, call):
        try:
            print(call)
            print(call().__doc__)
            response = call()
        except ConnectionError:
            pass
        except: #different exceptions such as req limit, no internet connection
            #output to error log
            print(sys.exc_info())
            print('here')
            sys.exit()
        #log request and response
        return self.filter_response(response) #Pass by ref or val
        #return response#.json()

    # Abstract Methods
    def log_request(self):
        raise NotImplementedError()

    def log_response(self):
        raise NotImplementedError()

    def log_error(self):
        raise NotImplementedError()

    def filter_response(self, response):
        raise NotImplementedError()
