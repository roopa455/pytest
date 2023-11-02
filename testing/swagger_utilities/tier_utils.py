import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging

_logger = logging.getLogger("Utilities")

class Tier_Utils():

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


    def add_new_tier(self, network_id: str, tier_id: str) -> bool:
        if self.get_specific_tier(network_id, tier_id):
            logging.info(f"{self.t} tier_id {tier_id} already exists for network_id {network_id}")
            return False

        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/tiers"
        try:
            print(url)
            with open("../test_data/create_tier.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["id"] = tier_id
               body = json.dumps(json_data).encode('utf-8')
            self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
            response = self.connection.getresponse()
            logging.info(response.status)
            logging.info(str(response.read()))

            if response.status == 201:
                logging.info(f"{self.t} new tier added successfully")
                return True
            else:
               return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add tier: {e}")

        return False

    def get_specific_tier(self, network_id: str, tier_id) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/tiers/{tier_id}"
        try:
            print(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)
            if response.status == 200:
                logging.info(f"{self.t} get tier {tier_id} success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get network : {e}")
        return False


    def delete_specific_tier(self, network_id: str, tier_id) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/tiers/{tier_id}"
        try:
            print(url)
            self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)
            if response.status == 204:
                logging.info(f"{self.t} get tier {tier_id} success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get network : {e}")
        return False

