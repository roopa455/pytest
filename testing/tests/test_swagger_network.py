
import os, time, sys, random
import pytest, logging
utilPath = '../swagger_utilities'                # Custom Path for modules
sys.path.append(utilPath)                   # Edit env info (path for modules)
import network_utils as utils                   # Import our own modules
NetwrokUtils = utils.Network_Utils()                # Instantiate the class

def tc_head(msg, log_loc = ""):
    NetworkUtils.prPurple(f'\nStarting test for {msg} E2E Workflow')

def tc_tail(msg):
    global startTime
    startTime = int(time.time())
    endTime = int(time.time())
    elapsedTime = endTime - startTime
    NetworkUtils.prPurple(f'Completed test for {msg} E2E Workflow in {elapsedTime} seconds')

@pytest.mark.swagger_network
def test_swagger_add_new_network(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        assert NetworkUtils.add_new_network(network_id, name) is True, tc_tail('added new network')
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

@pytest.mark.swagger_network
def test_swagger_get_new_network(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        time.sleep(15)
        assert NetworkUtils.get_specific_network(network_id), tc_tail('get specific network')
        logging.INFO(f"getting the specific network_id {network_id} is successfull")
        assert SwaggerUtils.add_new_tier(network_id, tier_id), tc_tail('add new tier')
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

@pytest.mark.swagger_network
def test_swagger_update_network(setup_env):
    mcc = "200"
    mnc = "45"
    network_id, name, tier_id, gateway_id = setup_env
    try:
        time.sleep(15)
        assert NetworkUtils.update_specific_network(network_id, mcc, mnc), tc_tail('update specific network')
        SwaggerUtils.prGreen(f"updated the specific network id {network_id} successfully")
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

@pytest.mark.swagger_network
def test_swagger_delete_network(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        time.sleep(15)
        assert NetworkUtils.delete_specific_network(network_id), tc_tail('delete specific network')
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

def test_run_swagger_workflows():
    test_swagger_add_new_network(setup_env)
    test_swagger_get_new_network(setup_env)
    test_swagger_update_network(setup_env)
    test_swagger_delete_network(setup_env)


