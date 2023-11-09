import json
import logging
import os
import re
from typing import List, Any

#TODO: Exception safety

# Base Api, which will be used to initialise other specific apies
class Api:
    # Initialise with client_key, client_secret, host, device_id, device_name
    def __init__(self, key: str = None, secret: str = None, host: str = None,
                 device_id: str = None, device_name: str = None):
        self.key = key
        self.secret = secret
        self.host = host
        self.device_id = device_id
        self.device_name = device_name

    # Saving info about Api to cache
    def __save_to_cache(self, host: List[Any]):
        data = dict()
        data['apiKey'] = self.key
        data['apiSecret'] = self.secret
        data['host'] = self.host
        data['deviceId'] = self.device_id
        data['deviceName'] = self.device_name

        write_api = open(f'cache/Api{host[3]}.json', 'w')
        json.dump(data, write_api)
        write_api.close()

    # Load info about Api info
    def login(self, host: str):
        # Load info from JSON-file
        host = host.replace('.', '')
        host = re.split('[/:]', host)
        if os.path.exists(f'cache/Api{host[3]}.json'):
            api = open(f'cache/Api{host[3]}.json')
            data = json.load(api)
            self.key = data['apiKey']
            self.secret = data['apiSecret']
            self.host = data['host']
            if 'deviceId' in data:
                self.device_id = data['deviceId']
            else:
                logging.warning('No device id')
            if 'deviceName' in data:
                self.device_name = data['deviceName']
            else:
                logging.warning('No device name')
            api.close()
        # Load info from console and save it to cache
        else:
            print("Enter api key:")
            self.key = input()
            print("Enter api secret:")
            self.secret = input()
            print("Enter api host:")
            self.host = input()
            print("Enter device id:")
            self.device_id = input()
            print("Enter device name:")
            self.device_name = input()

            self.__save_to_cache(host)
