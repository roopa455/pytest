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

import os
import sys

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


class network_Get_EPC_configuration(unittest.TestCase):
    def test_setup(self):
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']

        console.write("Start Get Network EPC configuration setup")
        console.write("End Get Network EPC  configuration setup")
    @staticmethod
    def test_get_network():
        console.write("Starting  get Network EPC configuration test:\n")
        log_file.write("Starting  get Network EPC configuration test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']

        rGet = requests.get(url=(values['url'] + "lte/test-only/cellular/epc"), cert=(cert_path, key_path), verify=False)
        console.write(str(rGet.text))
        log_file.write(str(rGet.text))
        if rGet.status_code == 200:
            console.write("Get network passed. The current status:\n")
            console.write(str(rGet.status_code))
            log_file.write("Get network passed. The current status:\n")
            log_file.write(str(rGet.status_code))
        else:
            console.write("Get Network EPC  failed. The current status is not 200 (OK) and it is:\n ")
            log_file.write("Get Network EPC  failed. The current status is not 200 (OK) and it is:\n ")
            console.write(str(rGet))
            log_file.write(str(rGet))

    def test_tearDown(self):

        time.sleep(5)
        console.write("\nGet Network EPC  ended\n")
        log_file.write("\nGet Network EPC  ended\n")
        log_file.close()
        console.flush()

        print("Test ended.")


if __name__ == "__main__":
    unittest.main()
