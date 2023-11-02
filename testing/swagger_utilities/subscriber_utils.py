import sys, time, requests, os.path, json           # In-build modules
jsonPath = '../test_data'                 # Custom Path for modules
sys.path.append(jsonPath)
from test_data import test_data
#import test_data
import ssl
import http.client, subprocess
import logging

_logger = logging.getLogger("Utilities")

class Subscriber_Utils():

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

    def add_new_subscriber(self, network_id: str, apn_name: str, policy_name: str, subscriber_id: str) -> bool:
        if self.get_specific_subscriber(network_id, subscriber_id):
            logging.info(f"{self.t} subscriber_id {subscriber_id} in network {network_id} already exists")
            return False

        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/subscribers"
        try:
            print(url)
            with open("../test_data/add_subscriber.json", "r") as json_file:
                 subscriber_data = json.load(json_file)
        
            subscriber_data[0]["id"] = subscriber_id
            subscriber_data[0]["active_policies"] = [policy_name]
            subscriber_data[0]["active_apns"] = [apn_name]
            body = json.dumps(subscriber_data).encode('utf-8')
        
            self.connection.request(method="POST", url=url, headers=self.json_data.headers, body=body)
            response = self.connection.getresponse()
            logging.info(response.status)
            print(response.status)
            logging.info(str(response.read()))
            print(str(response.read()))

            if response.status == 201:
               logging.info(f"{self.t} new subscriber added successfully")
               return True
            else:
               return False
        except requests.exceptions.RequestException as e:
           logging.error(f"{self.t} Failed to add new subscriber: {e}")

        return False

    def add_multiple_subscribers(self, network_id: str, apns_list, policies_list, ids_list) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/subscribers"
        try:
            for apns, policies, subscriber_id in zip(apns_list, policies_list, ids_list):
                if self.get_specific_subscriber(network_id, subscriber_id):
                    logging.info(f"{self.t} subscriber_id {subscriber_id} in network {network_id} already exists")
                    continue
    
                with open("../test_data/add_subscriber.json", "r") as json_file:
                    subscriber_data = json.load(json_file)
    
                subscriber_data[0]["id"] = subscriber_id
                subscriber_data[0]["active_policies"] = [policies]
                subscriber_data[0]["active_apns"] = [apns]
                body = json.dumps(subscriber_data).encode('utf-8')
    
                self.connection.request(method="POST", url=url, headers=self.json_data.headers, body=body)
                response = self.connection.getresponse()
                logging.info(response.status)
                print(response.status)
                logging.info(str(response.read()))
                print(str(response.read()))
    
                if response.status == 201:
                    logging.info(f"{self.t} new subscriber {subscriber_id} added successfully")
                else:
                    logging.error(f"{self.t} Failed to add new subscriber {subscriber_id}")
    
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to add new subscribers: {e}")
    
    def list_all_subscribers(self, network_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/subscribers"
        try:
            logging.info(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)

            if response.status == 200:
                logging.info(f"{self.t} get specific subscribers for network {network_id} is success")
                return True
            else:
               return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get subscribers for network {network_id}  : {e}")

        return False

    def update_specific_subscriber(self, network_id: str, apn_name: str, policy_name: str, subscriber_id) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/subscribers/{subscriber_id}"
        try:
           logging.info(url)
           with open("../test_data/add_subscriber.json", "r") as json_file:
               json_data = json.load(json_file)
               json_data["active_apns"] = apn_name
               json_data["active_policies"] = policy_name
               body = json.dumps(json_data).encode('utf-8')
           self.connection.request(method="PUT", url = url, headers = self.json_data.headers, body=body)
           response = self.connection.getresponse()
           logging.info(response.status)
           logging.info(str(response.read()))

           if response.status == 204:
               logging.info(f"{self.t} update subscirber {subscriber_id} successfully")
               return True
           else:
              return False
        except requests.exceptions.RequestException as e:
            logging.info(f"{self.t} Failed to update subscriber {subscriber_id} : {e}")

        return False

    def get_specific_subscriber(self, network_id: str, subscriber_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/subscribers/{subscriber_id}"
        try:
            logging.info(url)
            self.connection.request(method="GET", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(str(response.read()))
            logging.info(response.status)

            if response.status == 200:
                logging.info(f"{self.t} get specific subscriber {subscriber_id} is success")
                return True
            else:
               return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to get subscriber {subscriber_id} : {e}")

        return False

    def delete_specific_subscriber(self, network_id: str, subscriber_id: str) -> bool:
        url = f"http://{self.hostIP}:{self.hostPort}/magma/v1/lte/{network_id}/subscribers/{subscriber_id}"
        try:
            logging.info(url)
            self.connection.request(method="DELETE", url = url, headers = self.json_data.headers)
            response = self.connection.getresponse()
            logging.info(response.status)

            if response.status == 204:
                logging.info(f"{self.t} delete subscriber {subscriber_id} is success")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"{self.t} Failed to delete subscriber {subscriber_id}  : {e}")
        return False

#sub_utils = Subscriber_Utils()
#sub_utils.add_new_subscriber("lte_network_674", "test_apn_674", "test_policy_674", "IMSI001010000000671")
#sub_utils.get_specific_subscriber("lte_network_674", "IMSI001010000000671")
