import backend.configs.package as module
import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *

logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\logs\\"
# create directory with the current date and time
module.os.makedirs(log_file_path + f"{execution_date}", exist_ok=True)
# Open log file with current execution date
file_name = module.os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"
console = module.sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = module.yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = module.yaml.safe_load(file)


class Get_base_name(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_get_apn(self):
        print("Starting Get Base Name test...")
        log_file.write("\nStarting Get Base Name test...\n\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        # Send get request
        rGet = requests.get(url=(values['url'] + f"network/test1/policies/base_names"), cert=(cert_path, key_path), verify=False)
        print("\nResponse body:" + str(rGet.text))
        log_file.write("\nResponse body:\n" + str(rGet.text))

        if rGet.status_code == 200:
            self.assertTrue(rGet.status_code, 200)
            print("Get Base Name passed. The Response code is: ")
            print(str(rGet.status_code))
            log_file.write("\nGet Base Name Test passed. The Response code is: ")
            log_file.write(str(rGet.status_code))
        else:
            self.assertTrue(rGet.status_code, 200)
            print("Get Base Name Test failed. The Response code is not 200 (OK) and it is: ")
            log_file.write("Get Base Name Test failed. The Response code is not 200 (OK) and it is: ")
            print(str(rGet.status_code))
            log_file.write(str(rGet.status_code))

    def tearDown(self):

        time.sleep(5)
        print("Get Base Name Test ended")
        log_file.write("\n\nGet Base Name Test ended\n")
        print(f"Report stored at:\n{log_file_path}")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
