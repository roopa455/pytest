import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *
urllib3.disable_warnings()
logging.captureWarnings(True)
logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + f'\\reports\logs\\'
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



class network (unittest.TestCase):
    def setup(self):
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        urllib3.disable_warnings()

    
    def test_get_description_network(self):
        print("Starting  get network Description test:\n")
        log_file.write("Starting  get network Description test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        print("Starting get test:")
        rGet = requests.get(url=(values['url']+"lte/test1"),cert=(cert_path, key_path), verify=False)
        print(rGet.text)
        if rGet.status_code == 200:
            self.assertEqual(rGet.status_code, 200)
            print("Test passed. The current status:", rGet)
        else:
            self.assertEqual(rGet.status_code, 200)
            print("Test failed. The current status is not 200 (OK) and it is ",  rGet)

    def tearDown(self):
        
        time.sleep(5)
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)
        logs = print(log.debug)
        
        print("Test ended.")
    



if __name__ == "__main__":
    unittest.main()
