import requests
import json
import configparser
import os
import constant

class Sweeps:
    def __init__(self):
        config = configparser.ConfigParser()
        if os.path.isfile('config.ini'):
            configfile = config.read('config.ini')
            config.read('config.ini')
            self.key = config['User']['APIkey']
        else:
            print("Config.ini not found. Creating with default values and fresh API key\n")
            APIKey = requests.get(constant.BASE_URL + "getNewAPIKey").json()
            print(APIKey)
            config.read('config.ini')
            config['User'] = {'APIKey': APIKey,
                              'bois': []}

            with open('config.ini', 'w') as configfile:
                config.write(configfile)

    def getmybois(self):
        body = json.dumps({'key': self.APIKey})
        bois = requests.put(constant.BASE_URL + "getMyBois", body)
        self.bois = bois
        return bois

    @staticmethod
    @property
    def worldmap():
        m = requests.get(constant.BASE_URL + "getMap").json()

        return m
        

