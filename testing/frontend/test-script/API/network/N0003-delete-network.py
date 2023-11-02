import requests
import yaml
from requests.auth import HTTPDigestAuth
import json
import urllib3
from datetime import *
import time
import unittest
import logging
import sys
from http.client import HTTPConnection  # py3
urllib3.disable_warnings()
logging.captureWarnings(True)
import os

logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 4)[0]
execution_date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\"
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)



class network (unittest.TestCase):
    def setup(self):
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        urllib3.disable_warnings()

    
    def test_network_delete(self):
        print("Starting delete test:")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        rdelete = requests.delete(url=(values['url']+"/lte/test1"),cert=(cert_path, key_path), verify=False)
        print(rdelete.text)
        if rdelete.status_code == 200:
            print("Test passed. The current status:", rdelete)
        else:
            print("Test failed. The current status is not 200 (OK) and it is ",  rdelete)

    def tearDown(self):
        
        time.sleep(5)
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)
        logs = print(log.debug)
        
        print("Test ended.")
    



if __name__ == "__main__":
    unittest.main()
