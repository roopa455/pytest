# import required packages from package.py module
import backend.configs.package as module

module.logging.captureWarnings(True)
# Get root directory of the project
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
# Open config files from configs directory
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = module.yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = module.yaml.safe_load(file)


class Get_APN(module.unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_get_apn(self):
        console.write("\nStarting Get APN test...\n\n")
        log_file.write("\nStarting Get APN test...\n\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network_apn = user_values['network_apn']
        # Send get request
        rGet = module.requests.get(url=(values['url'] + f"lte/{network_apn}/apns"), cert=(cert_path, key_path), verify=False)
        console.write("\nResponse body:\n" + str(rGet.text))
        log_file.write("\nResponse body:\n" + str(rGet.text))
        # Response validation
        if rGet.status_code == 200:
            console.write("\nGet APN Test passed. The Response code is: ")
            console.write(str(rGet.status_code))
            log_file.write("\nGet APN Test passed. The Response code is: ")
            log_file.write(str(rGet.status_code))
        else:
            console.write("Get APN Test failed. The Response code is not 200 (OK) and it is: ")
            log_file.write("Get APN Test failed. The Response code is not 200 (OK) and it is: ")
            console.write(str(rGet.status_code))
            log_file.write(str(rGet.status_code))

    def tearDown(self):

        module.time.sleep(5)
        console.write("\n\nGet APN Test ended\n")
        log_file.write("\n\nGet APN Test ended\n")
        console.write(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    module.unittest.main()
