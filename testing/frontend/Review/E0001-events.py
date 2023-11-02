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


class test_Get_Event(unittest.TestCase):
    def test_setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_get_events(self):
        console.write("Starting  get Query Events test:\n")
        log_file.write("Starting  get Query Events test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network = user_values['network']
        streams = user_values['streams']
        events = user_values['events']
        tags =  user_values['tags']
        hw_ids = user_values['hw_ids']
        Efrom = user_values['from']
        size = user_values['size']
        start = user_values['start']
        end =  user_values['end']
        # Send get request
        rGet = requests.get(url=(values['url'] + f"events/test1?streams={streams}&events={events}&tags={tags}&hw_ids={hw_ids}&from={Efrom}&size={size}&start={start}&end={end}"), cert=(cert_path, key_path), verify=False)
        console.write(str(rGet.text))
        log_file.write(str(rGet.text))
        if rGet.status_code == 200:
            console.write("Get query Events passed. The current status:\n")
            console.write(str(rGet.status_code))
            log_file.write("Get query Events passed. The current status:\n")
            log_file.write(str(rGet.status_code))
        else:
            console.write("Get query Events failed. The current status is not 200 (OK) and it is:\n ")
            log_file.write("Get query Events failed. The current status is not 200 (OK) and it is:\n ")
            console.write(str(rGet))
            log_file.write(str(rGet))

    def test_tearDown(self):

        time.sleep(5)
        console.write("\nGet Query Events ended\n")
        log_file.write("\nGet Query Events ended\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    unittest.main()
