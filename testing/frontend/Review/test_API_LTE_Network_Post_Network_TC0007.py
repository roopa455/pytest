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
from http.client import HTTPConnection  # py3

import os

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


class Post_Network(unittest.TestCase):

    def test_setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        print("Start Post Network setup")
        print("End Post Network setup")

    @staticmethod
    def test_post_network():
        print("test")
        console.write("\nStarting Post Network test:\n")
        log_file.write("\nStarting Post Network test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_add_network']

        rpost = requests.post(url=(values['url'] + f"lte/"), cert=(cert_path, key_path), json=json_path,
                              verify=False)
        console.write(str(rpost.text))
        log_file.write(str(rpost.text))
        if rpost.status_code == 201:
            console.write("\nPost Network Test passed. The response code is:\n")
            console.write(str(rpost.status_code))
            log_file.write("\nPost Network Test passed. The response code is:\n")
            log_file.write(str(rpost.status_code))
        else:
            console.write("Post Network Test failed. The response code  is:\n")
            log_file.write("Post Network Test failed. The response code is:\n")
            console.write(str(rpost.status_code))
            log_file.write(str(rpost.status_code))

        # verify the created APN is present using get command
        console.write("\n\nVerifying added Network is present:\n")
        log_file.write("\n\nVerifying added Network is present:\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"lte/"), cert=(cert_path, key_path), verify=False)
        if rGet.status_code == 200:
            console.write(f"\nNetwork is added as expected. \n")
            log_file.write(f"\nNetwork is added as expected. \n")

        else:
            console.write(f"\nNetwork is not added. \n ")
            log_file.write(f"\nNetwork is not added. \n ")

    def test_tearDown(self):

        time.sleep(5)
        console.write("\nPost APN Test ended\n")
        log_file.write("\nPost APN Test ended\n")
        console.write(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    unittest.main()
