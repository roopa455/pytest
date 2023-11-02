import requests
import yaml
from datetime import *
import time
import unittest
import logging
import sys
import os
import json

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


class Delete_Network(unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_delete_network(self):
        console.write("\nStarting Delete Nw test:\n")
        log_file.write("\nStarting Delete Nw test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']

        network_test = user_values['network_test']
        

        rDelete = requests.delete(url=(values['url'] + f"lte/{network_test}"), cert=(cert_path, key_path), verify=False)
        console.write(str(rDelete.text))
        log_file.write(str(rDelete.text))
        if rDelete.status_code == 204:
            console.write("\n Delete Nw Test passed. The response code is:\n")
            console.write(str(rDelete.status_code))
            log_file.write("\nDelete Nw Test passed. The response code is:\n")
            log_file.write(str(rDelete.status_code))
        else:
            console.write(" Delete Nw Test failed. The response code  is:\n")
            log_file.write(" Delete Nw Test failed. The response code is:\n")
            console.write(str(rDelete.status_code))
            log_file.write(str(rDelete.status_code))







    def tearDown(self):

        time.sleep(5)
        console.write("\nTest ended\n")
        log_file.write("\nTest ended\n")
        console.write(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    unittest.main()
