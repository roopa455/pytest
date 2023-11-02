import backend.configs.package as module

module.urllib3.disable_warnings()
module.logging.captureWarnings(True)

module.logging.captureWarnings(True)
# Get root directory of the project
root_dir = module.os.path.dirname(module.os.path.realpath(__file__)).rsplit(module.os.sep, 2)[0]
# Open log file with execution date
execution_date = module.datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\\"
file_name = module.os.path.basename(__file__)
log_file_path = log_file_path + f"{file_name}-{execution_date}.txt"
console = module.sys.stdout
log_file = open(log_file_path, 'w')
# Open config files
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = module.yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = module.yaml.safe_load(file)