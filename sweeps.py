import requests
import json
import configparser
import os
import constant
from constant import API_PATH

class Sweeps:
    def __init__(self):
        config = configparser.ConfigParser()
        if os.path.isfile('config.ini'):
            configfile = config.read('config.ini')
            config.read('config.ini')
            self.key = config['User']['APIkey']
        else:
            print("Config.ini not found. Creating with default values and fresh API key\n")
            print("Please enter a username")
            username = input()
            print("Please enter your email")
            email = input()
            APIKey = requests.put(constant.BASE_URL + "getNewAPIKey", data=json.dumps({"email": email})).json()
            config.read('config.ini')
            config['User'] = {'APIKey': APIKey,
                              'Username': username,
                              'Email': email,
                              'bois': []}

            with open('config.ini', 'w') as configfile:
                config.write(configfile)


    # method to avoid having to manually make requests in each class
    # TODO: should this be static?
    def apicall(self, endpoint, extension=None, sectorID=None, boiID=None, command=None, direction=None, headers=None):
		path = constant.API_PATH[endpoint]
        url = ""
        body = {}
		if headers == None:
			headers = {"content-type": "application/json"}
        if "{{key}}" in path:
            url = constant.BASE_URL + path.format(self.key)
        if "{{id}}" in path:
            if endpoint == "command":
                url = constant.BASE_URL + path.format(boiID)
                body = json.dumps({"APIKey": selp.key, "direction": direction, "command": command})
			if endpoint == "sector":
				url = path.format(sectorID)
				body =

		err = requests.put(url, data=body, header=headers)





    @staticmethod
    def getmapsize():
        m = requests.get(constant.BASE_URL + "getMap").json()
        return m

    @staticmethod
    def getsector(x, y):
        print(x + " " + y)

    def getownedboiz(self):
        body = json.dumps({'key': self.APIKey})
        bois = requests.put(constant.BASE_URL + "getMyBois", body)
        self.bois = bois
        return bois
