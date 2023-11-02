# import required packages from package.py module
import backend.configs.package as module



module.logging.captureWarnings(True)
root_dir = module.os.path.dirname(module.os.path.realpath(__file__)).rsplit(module.os.sep, 4)[0]
execution_date = module.datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\"
# create directory with the current date and time
module.os.makedirs(log_file_path+f"{execution_date}",exist_ok = True)
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


class Post_APN(module.unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_post_apn(self):
        console.write("\nStarting Post APN test:\n")
        log_file.write("\nStarting Post APN test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_add_apn']
        network_apn = user_values['network_apn']
        apn_name = user_values['apn_name']
        with open(f'{json_path}', 'r') as f:
            json_data_obj = module.json.load(f)
        rPost = module.requests.post(url=(values['url'] + f"lte/{network_apn}/apns"), cert=(cert_path, key_path), json=json_data_obj, verify=False)
        console.write(str(rPost.text))
        log_file.write(str(rPost.text))
        if rPost.status_code == 201:
            console.write("\nPost APN Test passed. The response code is:\n")
            console.write(str(rPost.status_code))
            log_file.write("\nPost APN Test passed. The response code is:\n")
            log_file.write(str(rPost.status_code))
        else:
            console.write("Post APN Test failed. The response code  is:\n")
            log_file.write("Post APN Test failed. The response code is:\n")
            console.write(str(rPost.status_code))
            log_file.write(str(rPost.status_code))

        # verify the created APN is present using get command
        console.write("\n\nVerifying added APN is present:\n")
        log_file.write("\n\nVerifying added APN is present:\n")
        module.time.sleep(5)
        rGet = module.requests.get(url=(values['url'] + f"lte/{network_apn}/apns/{apn_name}"), cert=(cert_path, key_path), verify=False)
        if rGet.status_code == 200:
            console.write(f"\nAPN {apn_name} is added as expected. \n")
            log_file.write(f"\nAPN {apn_name} is added as expected. \n")

        else:
            console.write(f"\nAPN {apn_name} is not added. \n ")
            log_file.write(f"\nAPN {apn_name}is not added. \n ")


    def tearDown(self):

        module.time.sleep(5)
        console.write("\nPost APN Test ended\n")
        log_file.write("\nPost APN Test ended\n")
        console.write(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    module.unittest.main()
