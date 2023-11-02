import requests
import yaml
from datetime import *
import time
import unittest
import logging
import sys
import os

logging.captureWarnings(True)
# Get root directory of the project
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 4)[0]
# Open log file with execution date
execution_date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\"
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
# Open config files
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Get_Post_Gateway_cef(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']


    def test_delete_cwf(self):
        console.write("Starting  delete  CWF Getaway test:\n")
        log_file.write("Starting  delete  CWF Getaway  test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network = user_values['network']
        json_data = values['json_add_cwf']
        gateway_id = values['gateway_id']

        # Send get request
        rDelete = requests.delete(url=(values['url'] + f"/cwf/{network}/gateways/{gateway_id}"), cert=(cert_path, key_path))
        console.write(str(rDelete.text))
        log_file.write(str(rDelete.text))
        if rDelete.status_code == 200:
            console.write("Delete CWF Getaway passed. The current status:\n")
            console.write(str(rDelete.status_code))
            log_file.write("delete CWF Getaway passed. The current status:\n")
            log_file.write(str(rDelete.status_code))
        else:
            console.write("Delete CWF Getaway failed. The current status is not 200 (OK) and it is:\n ")
            log_file.write("Delete CWF Getaway failed. The current status is not 200 (OK) and it is:\n ")
            console.write(str(rDelete))
            log_file.write(str(rDelete))


    def test_get_cwf(self):
        console.write(" list CWF Getaway test:\n")
        log_file.write(" List CWF Getaway  test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network = user_values['network']
       # Send get request
        rGet = requests.get(url=(values['url'] + f"/cwf/{network}/gateways"), cert=(cert_path, key_path), verify=False)
        console.write(str(rGet.text))
        log_file.write(str(rGet.text))
        if rGet.status_code == 200:
            console.write("List CWF Getaway passed. The current status:\n")
            console.write(str(rGet.status_code))
            log_file.write("List CWF Getaway passed. The current status:\n")
            log_file.write(str(rGet.status_code))
        else:
            console.write("List CWF Getaway failed. The current status is not 200 (OK) and it is:\n ")
            log_file.write("List CWF Getaway failed. The current status is not 200 (OK) and it is:\n ")
            console.write(str(rGet))
            log_file.write(str(rGet))

    def tearDown(self):

        time.sleep(5)
        console.write("\nPost CWF Getaway ended\n")
        log_file.write("\nPost CWF Getaway ended\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    unittest.main()
