# import required packages from package.py module
import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *
logging.captureWarnings(True)
# Get root directory of the project
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\logs\\"
# create directory with the current date and time
os.makedirs(log_file_path+f"{execution_date}",exist_ok = True)
# Open log file with current execution date
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"
log_file = open(log_file_path, 'w')
# Open config files from configs directory
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Put_Subscribers(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']


    def test_put_subscribers(self):

        print("\nStarting Put Subscriber test...\n\n")
        log_file.write("\nStarting Put Subscriber test...\n\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_put_subscriber']
        network_subscriber = user_values['network_subscriber']
        subscriber_id = user_values['subscriber_id']
        with open(f'{json_path}', 'r') as f:
            json_data_obj = json.load(f)
        print(f"Subscriber Id to Edit: {subscriber_id}\n")
        log_file.write(f"Subscriber Id to Edit: {subscriber_id}\n")
        # Send put request
        # Changing Active policy in the subscriber
        print ("Changing Active policy in the subscriber\n")
        log_file.write("Changing Active policy in the subscriber\n")
        rPut = requests.put(url=(values['url'] + f"lte/{network_subscriber}/subscribers/{subscriber_id}"), cert=(cert_path, key_path), json=json_data_obj, verify=False)
        print("\nResponse body:\n" + str(rPut.text))
        log_file.write("\nResponse body:\n" + str(rPut.text))
        # Response validation
        if rPut.status_code == 204:
            print("\nPut Subscriber Test passed. The Response code is: ")
            print(str(rPut.status_code))
            log_file.write("\nPut Subscriber Test passed. The Response code is: ")
            log_file.write(str(rPut.status_code))
            self.assertEqual(rPut.status_code, 204)
        else:
            print("Put Subscriber Test failed. The Response code is not 200 (OK) and it is: ")
            log_file.write("Put Subscriber Test failed. The Response code is not 200 (OK) and it is: ")
            print(str(rPut.status_code))
            log_file.write(str(rPut.status_code))
            self.assertEqual(rPut.status_code, 204)

        # verify the modified Subscriber using the Get Subscriber command

        print("\n\nVerifying modified Subscriber :\n")
        log_file.write("\n\nVerifying modified Subscriber :\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"lte/{network_subscriber}/subscribers/{subscriber_id}"),
                                   cert=(cert_path, key_path), verify=False)
        print("\nResponse body:\n" + str(rGet.text))
        log_file.write("\nResponse body:\n" + str(rGet.text))
        if rGet.status_code == 200:
            print(f"\nSubscriber id {subscriber_id} is modified as expected. \n")
            log_file.write(f"\nSubscriber id {subscriber_id} is modified as expected. \n")
            self.assertEqual(rGet.status_code, 200)

        else:
            print(f"\nError in put Subscriber id: {subscriber_id}  \n ")
            log_file.write(f"\nError in put Subscriber id: {subscriber_id} \n ")
            self.assertEqual(rGet.status_code, 200)

    def tearDown(self):

        time.sleep(5)
        print("\n\nPut Subscriber Test ended\n")
        log_file.write("\n\nPut Subscriber Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()



if __name__ == "__main__":
    unittest.main()
