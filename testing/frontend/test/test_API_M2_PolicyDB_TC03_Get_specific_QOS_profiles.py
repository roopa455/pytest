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
os.makedirs(log_file_path + f"{execution_date}", exist_ok=True)
# Open log file with current execution date
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Get_QOS_profiles(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_get_specific_qos(self):
        print("Starting Get QOS Profiles test...")
        log_file.write("\nStarting Get QOS Profiles  test...\n\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        qos_profile = root_dir + user_values['qos_profile']
        # Send get request
        rGet = requests.get(url=(values['url'] + f"lte/test1/policy_qos_profiles/{qos_profile}/"),
                            cert=(cert_path, key_path), verify=False)
        print("\nResponse body:" + str(rGet.text))
        log_file.write("\nResponse body:\n" + str(rGet.text))

        if rGet.status_code == 200:
            self.assertTrue(rGet.status_code, 200)
            print("Get APN Test passed. The Response code is: ")
            print(str(rGet.status_code))
            log_file.write("\nGet QOS Profiles  Test passed. The Response code is: ")
            log_file.write(str(rGet.status_code))
        else:
            self.assertTrue(rGet.status_code, 200)
            print("Get QOS Profiles Test failed. The Response code is not 200 (OK) and it is: ")
            log_file.write("Get QOS Profiles Test failed. The Response code is not 200 (OK) and it is: ")
            print(str(rGet.status_code))
            log_file.write(str(rGet.status_code))

    def tearDown(self):

        time.sleep(5)
        print("Get QOS Profiles Test ended")
        log_file.write("\n\nGet QOS Profiles Test ended\n")
        print(f"Report stored at:\n{log_file_path}")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
