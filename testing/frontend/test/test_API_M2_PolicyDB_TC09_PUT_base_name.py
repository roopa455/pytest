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


class put_base_name(unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        print("Start the Put Qos Profiles setup")
        print("End the Put Qos Profiles setup")

    def test_put_base_name(self):
        print("\nStarting Put base name test:\n")
        log_file.write("\nStarting Put base name test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_put_base_name']
        network = 'test1'

        rPut = requests.put(url=(values['url'] + f"/networks/{network}/policies/base_names/test_base"), cert=(cert_path, key_path), verify=False)
        print(str(rPut.text))
        log_file.write(str(rPut.text))
        if rPut.status_code == 204:
            print("\nPut base name Test passed. The response code is:\n")
            print(str(rPut.status_code))
            log_file.write("\nPut base name Test passed. The response code is:\n")
            log_file.write(str(rPut.status_code))
        else:
            print("Put base name Test failed. The response code  is:\n")
            log_file.write("Put base name Test failed. The response code is:\n")
            print(str(rPut.status_code))
            log_file.write(str(rPut.status_code))



    def tearDown(self):

        time.sleep(5)
        print("\nPut base name Test ended\n")
        log_file.write("\nPut base nameTest ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
