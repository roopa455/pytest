import sys

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
logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_folder_path = root_dir + f'\\reports\logs\\'
file_name = os.path.basename(__file__)
log_file_path = log_folder_path + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)



class network (unittest.TestCase):
    def test_setup(self):
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        urllib3.disable_warnings()

    
    def test_get_description_network(self):
        print("Starting  get network Description test:\n")
        log_file.write("Starting  get network Description test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        print("Starting get test:")
        rGet = requests.get(url=(values['url']+"lte/test-only"),cert=(cert_path, key_path), verify=False)
        print(rGet.text)
        if rGet.status_code == 200:
            print("Test passed. The current status:", rGet)
        else:
            print("Test failed. The current status is not 200 (OK) and it is ",  rGet)

    def test_tearDown(self):
        
        time.sleep(5)
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)
        logs = print(log.debug)
        
        print("Test ended.")
    



if __name__ == "__main__":
    unittest.main()
