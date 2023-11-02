import backend.configs.package as module

module.logging.captureWarnings(True)
root_dir = module.os.path.dirname(module.os.path.realpath(__file__)).rsplit(module.os.sep, 2)[0]
execution_date = module.datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\"
file_name = module.os.path.basename(__file__)
log_file_path = log_file_path + f"{file_name}-{execution_date}.txt"
console = module.sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = module.yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = module.yaml.safe_load(file)


class Put_Network_EPC_Configuration(module.unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']
        console.write(print("Start the Put Network EPC Configuration setup"))
        console.write(print("End the Put Network EPC Configuration setup"))

    def test_put_apn(self):
        console.write("\nStarting Put Network EPC Configuration test:\n")
        log_file.write("\nStarting Put Network EPC Configuration  test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_put_epc']
        network = 'test-only'

        rPut = module.requests.put(url=(values['url'] + f"/lte/{network}/cellular/epc"), cert=(cert_path, key_path), verify=False)
        console.write(str(rPut.text))
        log_file.write(str(rPut.text))
        if rPut.status_code == 204:
            console.write("\nPut  Network EPC Configuration Test passed. The response code is:\n")
            console.write(str(rPut.status_code))
            log_file.write("\nPut Network EPC Configuration Test passed. The response code is:\n")
            log_file.write(str(rPut.status_code))
        else:
            console.write("Put Network EPC Configuration Test failed. The response code  is:\n")
            log_file.write("Put Network EPC Configuration Test failed. The response code is:\n")
            console.write(str(rPut.status_code))
            log_file.write(str(rPut.status_code))



    def tearDown(self):

        module.time.sleep(5)
        console.write("\nPut Network EPC Configuration  Test ended\n")
        log_file.write("\nPut Network EPC Configuration  Test ended\n")
        console.write(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()
        console.flush()


if __name__ == "__main__":
    module.unittest.main()
