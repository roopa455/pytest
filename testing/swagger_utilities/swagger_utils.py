import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging

_logger = logging.getLogger("Utilities")

class Swagger_Utils():

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


    def prRed(self, skk): print("\033[91m{}\033[00m" .format(skk))
    def prGreen(self, skk): print("\033[92m{}\033[00m" .format(skk))
    def prPurple(self, skk): print("\033[95m{}\033[00m" .format(skk))
    def prCyan(self, skk): print("\033[96m{}\033[00m" .format(skk))

    def add_new_network(self, id: str, name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte"
        try:
           print(url)
           with open("../test_data/add_network.json", "r") as json_file:
               #json_data = json_file.read()
               json_data = json.load(json_file)
               json_data["id"] = id
               json_data["name"] = name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)

           if response.status == 201:
               logging.info(f"{self.t} new network added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add network: {e}")

        return False

    def get_specific_network(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}"
        try:
            print(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info("response code", response.read())
            logging.info(response.status)
            if response.status == 200:
                logging.info(f"{self.t} get network success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get network : {e}")
        return False

    def update_specific_network(self, network_id: str, mcc: str, mnc: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}"
        try:
            print(url)
            with open("../test_data/update_network.json", "r") as json_file:
                json_data = json.load(json_file)
                json_data["mcc"] = mcc
                json_data["mnc"] = mnc
                body = json.dumps(json_data).encode('utf-8')
            print(body)
            self.connection.request(method="PUT", url = url, headers = self.json_data.headers, body=body)
            response = self.connection.getresponse()
            logging.info(response.status)
            if response.status == 204:
                logging.info(f"{self.t} update specific network success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to update network {network_id} : {e}")
        return False

    def delete_specific_network(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}"
        try:
            print(url)
            self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            print(response.status)
            
            if response.status == 204:
                logging.info(f"{self.t} delete network success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to delete network : {e}")
        return False

    def add_new_tier(self, network_id: str, id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/tiers"
        try:
            print(url)
            with open("../test_data/create_tier.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["id"] = id
               body = json.dumps(json_data).encode('utf-8')
            self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
            response = self.connection.getresponse()
            logging.info(response.status)

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
            logging.info("response code", response.read())
            logging.info(response.status)
            if response.status == 200:
                logging.info(f"{self.t} get tier {tier_id} success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get network : {e}")
        return False

    def add_new_gateway(self, network_id: str, hardware_id: str, key: str, id: str, tier_name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways"
        try:
           print(url)
           with open("../test_data/add_gateway.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["device"]["hardware_id"] = hardware_id
               json_data["device"]["key"]["key"] = key
               json_data["id"] = id
               json_data["tier"] = tier_name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           
           if response.status == 201:
               logging.info(f"{self.t} new gateway added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add new gateway: {e}")

        return False

    def update_specific_gateway(self, network_id: str, id: str, tier_name: str, name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/gateways/{id}"
        try:
           print(url)
           with open("../test_data/add_gateway.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["tier"] = tier_name
               json_data["name"] = name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="PUT", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)

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
            print(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info("response code",response.read())
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
            print(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info("response code",response.read())
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
            print(url)
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

    def add_new_apn(self, network_id: str, apn_name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns"
        try:
           print(url)
           with open("../test_data/add_apn.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["apn_name"] = apn_name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           if response.status == 201:
               logging.INFO(f"{self.t} new apn {apn_name} added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add apn {apn_name} : {e}")

        return False

    def get_specific_apn(self, network_id: str, apn_name: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns/{apn_name}"
        try:
           print(url)
           self.connection.request(method="GET", url = url, headers = self.json_data.headers)
           response = self.connection.getresponse()
           print(response.read())
           print(response.status)
           if response.status == 200:
               logging.info(f"{self.t} get apn {apn_name} is successfull")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add apn {apn_name} : {e}")

        return False

    def update_specific_apn(self, network_id: str, apn_name: str, max_bandwidth: int) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/apns/{apn_name}"
        try:
           print(url)
           with open("../test_data/update_apn.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["ambr"]["max_bandwidth_dl"] = max_bandwidth 
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.read())
           logging.info(response.status)
           if response.status == 204:
               logging.info(f"{self.t} updated apn {apn_name} successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to update apn {apn_name} : {e}")

        return False

    def add_new_policy(self, network_id: str, id: str, priority: int) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/networks/{network_id}/policies/rules"
        try:
           print(url)
           with open("../test_data/add_policy.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["id"] = id
               json_data["priority"] = priority
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="POST", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           print(response.status)

           if response.status == 201:
               self.prGreen(f"{self.t} new policy added successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            self.prRed(f"{self.t} Failed to add new policy: {e}")

        return False

