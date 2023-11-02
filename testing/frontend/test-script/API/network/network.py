import requests
import yaml
from requests.auth import HTTPDigestAuth
import json
import urllib3
from datetime import *
import time
import unittest
import logging
import os
from http.client import HTTPConnection  # py3
urllib3.disable_warnings()
logging.captureWarnings(True)



class network (unittest.TestCase):
    def setup(self):
        path = os.path.abspath(os.getcwd())
        dir_path = os.path.abspath(path+"/backend/configs")
        with open (f'{dir_path}/configs.yaml','r') as file:
            values = yaml.safe_load(file)

        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        urllib3.disable_warnings()

    
    def test_get(self):
        print("Starting get test:")
        rGet = requests.get(url=self.url,cert=(self.cert, self.key), verify=False)
        print(rGet.text)
        if rGet.status_code == 200:
            print("Test passed. The current status:", rGet)
        else:
            print("Test failed. The current status is not 200 (OK) and it is ",  rGet)



    def tearDown(self):
        
        time.sleep(5)
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)

        # logging from urllib3 to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        log.addHandler(ch)

        # print statements from `http.client.HTTPConnection` to console/stdout
        HTTPConnection.debuglevel = 1
        today = date.today()
        logs = print(log.debug)
        
        print("Test ended.")
    



if __name__ == "__main__":
    unittest.main()
