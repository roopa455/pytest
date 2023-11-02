import sys

import backend.configs.package as module
import os
module.urllib3.disable_warnings()
module.logging.captureWarnings(True)
module.logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = module.datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_folder_path = root_dir + f'\\reports\logs\\'
file_name = os.path.basename(__file__)
log_file_path = log_folder_path + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = module.yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = module.yaml.safe_load(file)



class network(module.unittest.TestCase):
    def setup(self):
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        module.urllib3.disable_warnings()

    def test_network_delete(self):
        print("Starting delete test:")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        rdelete = module.requests.delete(url=(values['url'] + "/lte/test1"), cert=(cert_path, key_path), verify=False)
        print(rdelete.text)
        if rdelete.status_code == 200:
            print("Test passed. The current status:", rdelete)
        else:
            print("Test failed. The current status is not 200 (OK) and it is ", rdelete)

    def tearDown(self):

        module.time.sleep(5)
        log = module.logging.getLogger('urllib3')
        log.setLevel(module.logging.DEBUG)
        logs = print(log.debug)

        print("Test ended.")


if __name__ == "__main__":
    module.unittest.main()
