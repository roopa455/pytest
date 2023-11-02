import requests
import yaml
from requests.auth import HTTPDigestAuth
import json
import urllib3
from datetime import *
import time
import unittest
import logging
from http.client import HTTPConnection  # py3
urllib3.disable_warnings()
logging.captureWarnings(True)
import os
dir_path = os.path.abspath("backend\configs")
with open (f'{dir_path}/configs.yaml','r') as file:
    values = yaml.safe_load(file)



class network (unittest.TestCase):
    def setup(self):


        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        urllib3.disable_warnings()

    def test_post_network(self):
        print("Starting post test:")
        rPost = requests.post(url=(values['url']+"lte"),cert=(values['cert'], values['key']),json=(values['json_add_network']),
        print(rPost.text)

    def tearDown(self):
        
        time.sleep(5)
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)
        logs = print(log.debug)
        
        print("Test ended.")
    



if __name__ == "__main__":
    unittest.main()
