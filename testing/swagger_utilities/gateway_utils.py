import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging

_logger = logging.getLogger("Utilities")

class Gateway_Utils():

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

    def add_new_gateway(self, network_id: str, hardware_id: str, key: str, gateway_id: str, tier_name: str) -> bool:
        
        # Check if the network already exists
        if self.get_specific_gateway(network_id, gateway_id):
            logging.info(f"{self.t} Network {network_id} already exists")
            return False

        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways"
        try:
           logging.info(url)
           with open("../test_data/add_gateway.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["device"]["hardware_id"] = hardware_id
               json_data["device"]["key"]["key"] = key
               json_data["id"] = gateway_id
               json_data["tier"] = tier_name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           logging.info(str(response.read()))
           
           if response.status == 201:
               logging.info(f"{self.t} new gateway {gateway_id} added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add new gateway: {e}")

        return False

    def update_specific_gateway(self, network_id: str, id: str, name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways/{id}"
        try:
           logging.info(url)
           with open("../test_data/add_gateway.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["name"] = name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="PUT", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           logging.info(str(response.read()))

           if response.status == 204:
               logging.info(f"{self.t} new gateway added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.info(f"{self.t} Failed to add new gateway: {e}")

        return False

    def get_specific_gateway(self, network_id: str, gateway_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways/{gateway_id}"
        try:
            logging.info(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)

            if response.status == 200:
                logging.info(f"{self.t} get specifc gateway is success")
                return True
            else:
               return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get gateway : {e}")

        return False

    def list_all_gateways(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways"
        try:
            logging.info(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)

            if response.status == 200:
                logging.info(f"{self.t} get specifc gateway is success")
                return True
            else:
               return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get gateway : {e}")

        return False

    def delete_specific_gateway(self, network_id: str, gateway_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways/{gateway_id}"
        try:
            logging.info(url)
            self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(response.status)

            if response.status == 204:
                logging.info(f"{self.t} delete network success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to delete network : {e}")
        return False


