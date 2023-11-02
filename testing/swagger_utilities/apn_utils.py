import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging
import urllib.parse

_logger = logging.getLogger("Utilities")

class Apn_Utils():

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

    def add_new_apn(self, network_id: str, apn_name: str) -> bool:
        # Check if the network already exists
        if self.get_specific_apn(network_id, apn_name):
            logging.info(f"{self.t} Network {network_id} already exists")
            return False
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns"
        try:
            logging.info(url)
            with open("../test_data/add_apn.json", "r") as json_file:
                json_data = json.load(json_file)
                json_data["apn_name"] = apn_name
            body = json.dumps(json_data).encode('utf-8')
            self.connection.request(method="POST", url=url, headers=self.json_data.headers, body=body)
            response = self.connection.getresponse()
            logging.info(response.status)
            logging.info(str(response.read()))
            if response.status == 201:
                logging.info(f"{self.t} New apn {apn_name} added succesfully")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add apn {apn_name} : {e}")

        return False

    def add_multiple_apns(self, network_id: str, apn_name: list) -> bool:
        # Check if the network already exists
        if self.get_specific_apn(network_id, apn_name):
            logging.info(f"{self.t} Network {network_id} already exists")
            return False
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns"
        try:
            logging.info(url)
            with open("../test_data/add_apn.json", "r") as json_file:
                json_data = json.load(json_file)
    
            successes = 0  # Count of successful additions
            for i in range(0, len(apn_name)):
                json_data["apn_name"] = apn_name[i]
                body = json.dumps(json_data).encode('utf-8')
                self.connection.request(method="POST", url=url, headers=self.json_data.headers, body=body)
                response = self.connection.getresponse()
                logging.info(response.status)
                logging.info(str(response.read()))
    
                if response.status == 201:
                    logging.info(f"{self.t} New apn {apn_name} added successfully")
                    successes += 1
    
            if successes == len(apn_name):
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add apn: {e}")
    
        return False

    def get_specific_apn(self, network_id: str, apn_name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns/{apn_name}"
        try:
           print(url)
           self.connection.request(method="GET", url = url, headers = self.json_data.headers)
           response = self.connection.getresponse()
           logging.info(str(response.read()))
           logging.info(response.status)
           if response.status == 200:
               logging.info(f"{self.t} get apn {apn_name} is successfull")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add apn {apn_name} : {e}")

        return False

    def update_specific_apn(self, network_id: str, apn_name: str, pdn_type: int) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns/{apn_name}"
        try:
           print(url)
           with open("../test_data/update_apn.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["apn_configuration"]["pdn_type"] = pdn_type 
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(str(response.read()))
           logging.info(response.status)
           if response.status == 204:
               logging.info(f"{self.t} updated apn {apn_name} successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to update apn {apn_name} : {e}")

        return False

    def delete_specific_apn(self, network_id: str, apn_name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns/{apn_name}"
        try:
           logging.info(url)
           self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
           response = self.connection.getresponse()
           logging.info(response.read())
           logging.info(response.status)
           if response.status == 204:
               logging.info(f"{self.t} delete apn {apn_name} is successfull")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to delete apn {apn_name} : {e}")

        return False
#apn_utils = Apn_Utils()
#apn_utils.add_multiple_apns("lte_network_698", ["test1", "test2"])
