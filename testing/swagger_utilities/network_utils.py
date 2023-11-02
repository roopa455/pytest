import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging

_logger = logging.getLogger("Utilities")

class Network_Utils():

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

    def add_new_network(self, network_id: str, name: str) -> bool:
        # Check if the network already exists
        if self.get_specific_network(network_id):
            logging.info(f"{self.t} Network {network_id} already exists")
            return False

        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte"
        try:
           logging.info(url)
           with open("../test_data/add_network.json", "r") as json_file:
               #json_data = json_file.read()
               json_data = json.load(json_file)
               json_data["id"] = network_id
               json_data["name"] = name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           logging.info(str(response.read()))

           if response.status == 201:
               logging.info(f"{self.t} new network {network_id} added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add network {network_id}: {e}")

        return False

    def get_specific_network(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}"
        try:
            logging.info(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)
            if response.status == 200:
                logging.info(f"{self.t} get network {network_id} successfully")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get network {network_id} : {e}")
        return False

    def update_specific_network(self, network_id: str, mcc: str, mnc: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}"
        try:
            logging.info(url)
            with open("../test_data/update_network.json", "r") as json_file:
                json_data = json.load(json_file)
                json_data["mcc"] = mcc
                json_data["mnc"] = mnc
                body = json.dumps(json_data).encode('utf-8')
            print(body)
            self.connection.request(method="PUT", url = url, headers = self.json_data.headers, body=body)
            response = self.connection.getresponse()
            logging.info(response.status)
            logging.info(str(response.read()))
            if response.status == 204:
                logging.info(f"{self.t} update specific network {network_id} success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to update network {network_id} : {e}")
        return False

    def delete_specific_network(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}"
        try:
            logging.info(url)
            self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(response.status)
            
            if response.status == 204:
                logging.info(f"{self.t} delete network {network_id} success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to delete network {network_id} : {e}")
        return False

