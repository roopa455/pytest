import requests
import yaml
from datetime import *
import time
import unittest
import logging
import sys
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


class Get_enodeb(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_get_enodeb(self):
        console.write("Starting Get enodeb test:\n")
        log_file.write("Starting Get Enodeb test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network_apn = user_values['network_apn']
        rGet = requests.get(url=(values['url'] + f"lte/{network_apn}/apns"), cert=(cert_path, key_path), verify=False)
        console.write(str(rGet.text))
        log_file.write(str(rGet.text))
        if rGet.status_code == 200:
            console.write("Get Enodeb Test passed. The current status:\n")
            console.write(str(rGet.status_code))
            log_file.write("Get Enodeb Test passed. The current status:\n")
            log_file.write(str(rGet.status_code))
        else:
            console.write("Get Enodeb Test failed. The current status is not 200 (OK) and it is:\n ")
            log_file.write("Get Enodeb Test failed. The current status is not 200 (OK) and it is:\n ")
            console.write(str(rGet))
            log_file.write(str(rGet))

    def tearDown(self):

        time.sleep(5)
        console.write("\nGet APN Test ended\n")
        log_file.write("\nGet APN Test ended\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    unittest.main()
