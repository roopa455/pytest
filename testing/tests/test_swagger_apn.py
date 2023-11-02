import os, time, sys, random
import pytest, logging
utilPath = '../swagger_utilities'                # Custom Path for modules
sys.path.append(utilPath)                   # Edit env info (path for modules)
import network_utils as utils                   # Import our own modules
NetworkUtils = utils.Network_Utils()                # Instantiate the class
import apn_utils as utils                   # Import our own modules
ApnUtils = utils.Apn_Utils()                # Instantiate the class
import logging
_logger = logging.getLogger("APN")

def tc_head(msg, log_loc = ""):
    logging.info(f'\nStarting test for {msg} E2E Workflow')

def tc_tail(msg):
    global startTime
    startTime = int(time.time())
    endTime = int(time.time())
    elapsedTime = endTime - startTime
    logging.info(f'Completed test for {msg} E2E Workflow in {elapsedTime} seconds')

@pytest.mark.swagger_apn
def test_swagger_add_new_apn(setup_env):
    pdn_type = 2
    network_id, name, tier_id, gateway_id, apn_name, policy_id, subscriber_id = setup_env
    try:
        assert NetworkUtils.add_new_network(network_id, name) is True, tc_tail('added new network')
        assert ApnUtils.add_new_apn(network_id, apn_name) is True, tc_tail('added new apn')
        assert ApnUtils.get_specific_apn(network_id, apn_name) is True, tc_tail('get new apn')
        assert ApnUtils.update_specific_apn(network_id, apn_name, pdn_type) is True, tc_tail('updated apn')
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

def test_swagger_apn_workflows():
    test_swagger_add_new_apn(setup_env)
