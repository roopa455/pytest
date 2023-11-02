
import os, time, sys, random
import pytest, logging, subprocess
utilPath = '../swagger_utilities'                # Custom Path for modules
sys.path.append(utilPath)                   # Edit env info (path for modules)
import gateway_utils as utils                   # Import our own modules
GatewayUtils = utils.Gateway_Utils()                # Instantiate the class

def tc_head(msg, log_loc = ""):
    GatewayUtils.prPurple(f'\nStarting test for {msg} E2E Workflow')

def tc_tail(msg):
    global startTime
    startTime = int(time.time())
    endTime = int(time.time())
    elapsedTime = endTime - startTime
    GatewayUtils.prPurple(f'Completed test for {msg} E2E Workflow in {elapsedTime} seconds')

@pytest.mark.swagger_gateway
@pytest.mark.swagger_add_gateway
def test_swagger_add_new_gateway(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    hardware_id = subprocess.run(["uuidgen"], capture_output=True, text=True).stdout.strip()
    key = "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEO1marbBnZCgxd1zmnMEqHPFrxbOwZJkCbEM688tXlOvUJjoVGhKhjoTVI0BDik/waMoM5aFFuRH/lv+QH/+n1sLGp1MEtcAFU2f2MGRZmnhyogCAcNTbZQTvuCMjMsSP"
    try:
        assert GatewayUtils.add_new_gateway(network_id, hardware_id, key, gateway_id, tier_id) is True, tc_tail("added new gateway")
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions
    finally:
        tc_tail('added new network')

@pytest.mark.swagger_gateway
@pytest.mark.get_specific_gateway
def test_get_specific_gateway(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        assert GatewayUtils.get_specific_gateway(network_id, gateway_id), tc_tail("get specific gateway")
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

@pytest.mark.swagger_gateway
@pytest.mark.list_all_gateways
def test_list_gateways_for_specific_network(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        assert GatewayUtils.list_all_gateways(network_id), tc_tail("list all gateways")
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

@pytest.mark.swagger_gateway
@pytest.mark.update_gateway
def test_update_specific_gateway(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        assert GatewayUtils.update_specific_gateway(network_id, gateway_id, tier_id, name), tc_tail("updated specific gateway")
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

@pytest.mark.swagger_gateway
@pytest.mark.delete_gateway
def test_delete_specific_gateway(setup_env):
    network_id, name, tier_id, gateway_id = setup_env
    try:
        assert GatewayUtils.delete_specific_gateway(network_id, gateway_id), tc_tail("deleted gateway")
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

def test_run_swagger_workflows():
    test_swagger_add_new_gateway()
    test_get_specific_gateway()
    test_list_gateways_for_specific_network()
    test_update_specific_gateway()
    test_delete_specific_gateway()
