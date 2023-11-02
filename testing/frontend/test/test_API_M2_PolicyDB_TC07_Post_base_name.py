import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *
logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\logs\\"
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


class post_base_name(unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_post_base_name(self):
        print("\nStarting Post Base name test:\n")
        log_file.write("\nStarting Post Base name test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_post_base_name']
        network = user_values['network']
        with open(f'{json_path}', 'r') as f:
            json_data_obj = json.load(f)
        rPost = requests.post(url=(values['url'] + f"networks/{network}/policies/base_names"),
                              cert=(cert_path, key_path), json=json_data_obj, verify=False)
        print(str(rPost.text))
        log_file.write(str(rPost.text))
        if rPost.status_code == 201:
            self.assertEqual(rPost.status_code, 201)
            print("\nPost Base name passed. The response code is:\n")
            print(str(rPost.status_code))
            log_file.write("\nPost Base name Test passed. The response code is:\n")
            log_file.write(str(rPost.status_code))
        else:
            print("Post Base name Test failed. The response code  is:\n")
            log_file.write("Post Base name Test failed. The response code is:\n")
            print(str(rPost.status_code))
            log_file.write(str(rPost.status_code))

        # verify the created APN is present using get command
        print("\n\nVerifying added Base name is present:\n")
        log_file.write("\n\nVerifying added Base name is present:\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"networks/{network}/policies/base_names"), cert=(cert_path, key_path),
                            verify=False)
        if rGet.status_code == 200:
            print(f"\nBase name is added as expected. \n")
            log_file.write(f"\nQOS Profiles is added as expected. \n")

        else:
            print(f"\nQOS Profiles is not added. \n ")
            log_file.write(f"\nBase name is not added. \n ")

    def tearDown(self):

        time.sleep(5)
        print("\nPost Base nameTest ended\n")
        log_file.write("\nPost Base name Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
