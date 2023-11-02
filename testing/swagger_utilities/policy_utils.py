import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging

_logger = logging.getLogger("Utilities")

class Policy_Utils():

    def __init__(self):
        self.json_data = test_data.json_data()
        self.hostIP = os.environ.get('hostIP')
        self.hostPort = os.environ.get('hostPort')
        self.cert_path = '../backend/configs/files/admin_operator.pem'
        self.key_path = '../backend/configs/files/admin_operator.key.pem'
        self.t = '    '
        # Initialize context and connection as class attributes
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        self.context.load_cert_chain(certfile=self.cert_path, keyfile=self.key_path, password='magma')
        self.connection = http.client.HTTPSConnection(self.hostIP, port=self.hostPort, context=self.context)

    def add_new_policy(self, network_id: str, id: str, priority: int) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/policies/rules"
        try:
           logging.info(url)
           with open("../test_data/add_policy.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["id"] = id
               json_data["priority"] = priority
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           logging.info(str(response.read()))

           if response.status == 201:
               logging.info(f"{self.t} new policy added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.info(f"{self.t} Failed to add new policy: {e}")

        return False

    def add_multiple_policies(self, network_id: str, ids: list, priority: int) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/policies/rules"
        try:
            logging.info(url)
            with open("../test_data/add_policy.json", "r") as json_file:
                json_data_template = json.load(json_file)
    
            successes = 0  # Count of successful additions
            for policy_id in ids:
                json_data = json_data_template.copy()
                json_data["id"] = policy_id
                json_data["priority"] = priority
                body = json.dumps(json_data).encode('utf-8')
                self.connection.request(method="POST", url=url, headers=self.json_data.headers, body=body)
                response = self.connection.getresponse()
                logging.info(response.status)
                logging.info(str(response.read()))
    
                if response.status == 201:
                    logging.info(f"{self.t} new policy {policy_id} added successfully")
                    successes += 1
    
            if successes == len(ids):
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add new policy: {e}")
    
        return False

    def get_specific_policy(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/policies/rules"
        try:
           logging.info(url)
           self.connection.request(method="GET", url = url, headers = self.json_data.headers)
           response = self.connection.getresponse()
           logging.info(response.status)
           logging.info(str(response.read()))

           if response.status == 200:
               logging.info(f"{self.t} new policy added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.info(f"{self.t} Failed to add new policy: {e}")

        return False

    def delete_specific_policy(self, network_id: str, rule_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/policies/rules/{rule_id}"
        try:
           logging.info(url)
           self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
           response = self.connection.getresponse()
           logging.info(response.status)

           if response.status == 204:
               logging.info(f"{self.t} new policy added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.info(f"{self.t} Failed to add new policy: {e}")

        return False

