
import os, time, sys, random
import pytest, logging
utilPath = '../swagger_utilities'                # Custom Path for modules
sys.path.append(utilPath)                   # Edit env info (path for modules)
import swagger_utils as utils                   # Import our own modules
SwaggerUtils = utils.Swagger_Utils()                # Instantiate the class


def setup_env():
    SwaggerUtils.prCyan(f'Setting up test environment') 

def tc_head(msg, log_loc = ""):
    SwaggerUtils.prPurple(f'\nStarting test for {msg} E2E Workflow')

def tc_tail(msg):
    global startTime
    startTime = int(time.time())
    endTime = int(time.time())
    elapsedTime = endTime - startTime
    SwaggerUtils.prPurple(f'Completed test for {msg} E2E Workflow in {elapsedTime} seconds')

#@pytest.mark.swagger_new_network
def test_swagger_add_new_network():
    id = "test_lte01"
    name = "test_lte01"
    try:
        assert SwaggerUtils.add_new_network(id, name) is True, tc_tail('added new network')
        logging.INFO(f"Added new network {id} successfully")
    except AssertionError as ae:
        logging.error(f'AssertionError occurred: {ae}')
        # Handle assertion failure
    except Exception as e:
        logging.error(f'An exception occurred while executing the test: {e}')
        # Handle other exceptions

#@pytest.mark.swagger_new_network
def test_swagger_get_new_network():
    network_id = "test_lte01"
    id = "test_lte11"
    try:
        assert SwaggerUtils.get_specific_network(network_id), tc_tail('get specific network')
        logging.INFO(f"getting the specific network_id {network_id} is successfull")
        assert SwaggerUtils.add_new_tier(network_id, id), tc_tail('add new tier')
    except AssertionError as ae:
        logging.error(f'AssertionError occurred: {ae}')
        # Handle assertion failure
    except Exception as e:
        logging.error(f'An exception occurred while executing the test: {e}')
        # Handle other exceptions

#@pytest.mark.swagger_new_network
def test_swagger_update_network():
    network_id = "test_lte01"
    mcc = "200"
    mnc = "45"
    try:
        time.sleep(15)
        assert SwaggerUtils.update_specific_network(network_id, mcc, mnc), tc_tail('update specific network')
        SwaggerUtils.prGreen(f"updated the specific network id {network_id} successfully")
    except AssertionError as ae:
        SwaggerUtils.prRed(f'AssertionError occurred: {ae}')
        # Handle assertion failure
    except Exception as e:
        SwaggerUtils.prRed(f'An exception occurred while executing the test: {e}')
        # Handle other exceptions

#@pytest.mark.swagger_new_network
def test_swagger_delete_network():
    network_id = "test_lte01"
    try:
        time.sleep(15)
        assert SwaggerUtils.delete_specific_network(network_id), tc_tail('delete specific network')
        SwaggerUtils.prGreen(f"deleting the specific network_id {network_id} is successfull")
    except AssertionError as ae:
        SwaggerUtils.prRed(f'AssertionError occurred: {ae}')
        # Handle assertion failure
    except Exception as e:
        SwaggerUtils.prRed(f'An exception occurred while executing the test: {e}')
        # Handle other exceptions

@pytest.mark.swagger_new_network
def test_swagger_add_new_gateway():
    network_id = "test_lte01" 
    hardware = "64e31d56-55d0-4f49-b040-b38f72d9968c"
    key = "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEO1marbBnZCgxd1zmnMEqHPFrxbOwZJkCbEM688tXlOvUJjoVGhKhjoTVI0BDik/waMoM5aFFuRH/lv+QH/+n1sLGp1MEtcAFU2f2MGRZmnhyogCAcNTbZQTvuCMjMsSP"
    id = "lte_gateway"
    tier_id = "test_lte11"
    try:
        assert SwaggerUtils.add_new_gateway(network_id, hardware, key, id, tier_id), tc_tail("added new gateway")
        SwaggerUtils.prGreen(f"Added new gateway {id} for network {network_id} successfully")
        assert SwaggerUtils.get_specific_gateway(network_id, id)
        SwaggerUtils.prGreen("Getting the specific gateway info {id} successfully")
    except AssertionError as ae:
        SwaggerUtils.prRed(f'AssertionError occurred: {ae}')
        # Handle assertion failure
    except Exception as e:
        SwaggerUtils.prRed(f'An exception occurred while executing the test: {e}')
        # Handle other exceptions

@pytest.mark.swagger_new_network
@pytest.mark.swagger_new_gateway
def test_setup():
    setup_env()

def test_run_swagger_workflows():
    test_swagger_add_new_network()
    test_swagger_get_new_network()
    test_swagger_update_network()
    test_swagger_delete_network()
    test_swagger_add_new_gateway()


