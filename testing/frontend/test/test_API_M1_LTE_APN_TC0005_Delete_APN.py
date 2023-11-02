import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *

logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\logs\\"
# create directory with the current date and time
os.makedirs(log_file_path + f"{execution_date}", exist_ok=True)
# Open log file with current execution date
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"

with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Delete_APN(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']

    def test_delete_apn(self):
        print("\nStarting Delete APN test:\n")
        log_file.write("\nStarting Delete APN test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network_apn = user_values['network_apn']
        apn_name = user_values['apn_name']
        rDelete = requests.delete(url=(values['url'] + f"lte/{network_apn}/apns/{apn_name}"),
                                         cert=(cert_path, key_path), verify=False)
        print("\nResponse body:\n" + str(rDelete.text))
        log_file.write("\nResponse body:\n" + str(rDelete.text))

        if rDelete.status_code == 204:
            print("\nDelete APN Test passed. The Response code is: ")
            print(str(rDelete.status_code))
            log_file.write("\nDelete APN Test passed. The Response code is: ")
            log_file.write(str(rDelete.status_code))
            self.assertEqual(rDelete.status_code, 204)
        else:
            print("\nDelete APN Test failed. The Response code is not 200 (OK) and it is: ")
            log_file.write("\nDelete APN Test failed. The Response code is not 200 (OK) and it is: ")
            print(str(rDelete.status_code))
            log_file.write(str(rDelete.status_code))
            self.assertEqual(rDelete.status_code, 204)

        # verify the APN is deleted using get command

        print("\n\nVerifying deleted APN is not present:\n")
        log_file.write("\n\nVerifying deleted APN is not present:\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"lte/{network_apn}/apns/{apn_name}"),
                                   cert=(cert_path, key_path),
                                   verify=False)

        if rGet.status_code != 200:
            print(f"\nAPN {apn_name} is deleted as expected\n")
            log_file.write(f"\nAPN {apn_name} is deleted as expected\n")
            self.assertNotEqual(rGet.status_code, 200)

        else:
            print(f"\nAPN {apn_name} is not deleted and is still present\n ")
            log_file.write(f"\nAPN {apn_name} is not deleted and is still present\n ")
            self.assertNotEqual(rGet.status_code, 200)

    def tearDown(self):

        time.sleep(5)
        print("\nDelete APN Test ended\n")
        log_file.write("\nDelete APN Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
