import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *
logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\logs\\"
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class put_network_epc_configuration(unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        print("Start the Put Network EPC Configuration setup")
        print("End the Put Network EPC Configuration setup")

    def test_put_apn(self):
        print("\nStarting Put Network EPC Configuration test:\n")
        log_file.write("\nStarting Put Network EPC Configuration  test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_put_epc']
        network = 'test-only'

        rPut = requests.put(url=(values['url'] + f"/lte/{network}/cellular/epc"), cert=(cert_path, key_path), verify=False)
        print(str(rPut.text))
        log_file.write(str(rPut.text))
        if rPut.status_code == 204:
            print("\nPut  Network EPC Configuration Test passed. The response code is:\n")
            print(str(rPut.status_code))
            log_file.write("\nPut Network EPC Configuration Test passed. The response code is:\n")
            log_file.write(str(rPut.status_code))
        else:
            print("Put Network EPC Configuration Test failed. The response code  is:\n")
            log_file.write("Put Network EPC Configuration Test failed. The response code is:\n")
            print(str(rPut.status_code))
            log_file.write(str(rPut.status_code))



    def tearDown(self):

        time.sleep(5)
        print("\nPut Network EPC Configuration  Test ended\n")
        log_file.write("\nPut Network EPC Configuration  Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
