
import os, time, sys, random
import pytest, logging, subprocess
utilPath = '../swagger_utilities'                # Custom Path for modules
sys.path.append(utilPath)                   # Edit env info (path for modules)
import network_utils as utils                   # Import our own modules
NetworkUtils = utils.Network_Utils()                # Instantiate the class
import gateway_utils as gw_utils
GatewayUtils = gw_utils.Gateway_Utils()
import apn_utils as apn_utils
ApnUtils = apn_utils.Apn_Utils()
import policy_utils as pc_utils
PolicyUtils = pc_utils.Policy_Utils()
import subscriber_utils as sub_utils
SubscriberUtils = sub_utils.Subscriber_Utils()
#from swagger_utilities.tier_utils import TierUtils
import tier_utils as tier_utils
TierUtils = tier_utils.Tier_Utils()

def tc_head(msg, log_loc = ""):
    NetworkUtils.prPurple(f'\nStarting test for {msg} E2E Workflow')

def tc_tail(msg):
    global startTime
    startTime = int(time.time())
    endTime = int(time.time())
    elapsedTime = endTime - startTime
    NetworkUtils.prPurple(f'Completed test for {msg} E2E Workflow in {elapsedTime} seconds')

@pytest.mark.swagger_subscriber
def test_swagger_add_new_subscriber(setup_env):
    network_id, name, tier_id, gateway_id, apn_name, policy_id, subscriber_id = setup_env
    priority = 9
    hardware_id = subprocess.run(["uuidgen"], capture_output=True, text=True).stdout.strip()
    key = "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEO1marbBnZCgxd1zmnMEqHPFrxbOwZJkCbEM688tXlOvUJjoVGhKhjoTVI0BDik/waMoM5aFFuRH/lv+QH/+n1sLGp1MEtcAFU2f2MGRZmnhyogCAcNTbZQTvuCMjMsSP"
    try:
        print("network", network_id, tier_id)
        assert NetworkUtils.add_new_network(network_id, name) is True, tc_tail('added new network')
        assert NetworkUtils.get_specific_network(network_id) is True, tc_tail('get specific network')
        assert TierUtils.add_new_tier(network_id, tier_id) is True, tc_tail('add new tier')
        assert TierUtils.get_specific_tier(network_id, tier_id) is True, tc_tail('add new tier')
        assert GatewayUtils.add_new_gateway(network_id, hardware_id, key, gateway_id, tier_id) is True, tc_tail("added new gateway")
        assert GatewayUtils.get_specific_gateway(network_id, gateway_id) is True, tc_tail("get specific gateway")
        assert ApnUtils.add_new_apn(network_id, apn_name) is True, tc_tail('added new apn')
        assert ApnUtils.get_specific_apn(network_id, apn_name) is True, tc_tail('get new apn')
        assert PolicyUtils.add_new_policy(network_id, policy_id, 9) is True, tc_tail('add new policy')
        assert PolicyUtils.get_specific_policy(network_id) is True, tc_tail('get policy')
        assert SubscriberUtils.add_new_subscriber(network_id, apn_name, policy_id, subscriber_id) is True, tc_tail('add new subscriber')
        assert SubscriberUtils.get_specific_subscriber(network_id, subscriber_id) is True, tc_tail('delete specific subscriber')
        assert SubscriberUtils.delete_specific_subscriber(network_id, subscriber_id) is True, tc_tail('delete specific subscriber')
        assert ApnUtils.delete_specific_apn(network_id, apn_name) is True, tc_tail('delete specific apn')
        assert GatewayUtils.delete_specific_gateway(network_id, gateway_id) is True, tc_tail('delete specific gateway')
        assert TierUtils.delete_specific_tier(network_id, tier_id) is True, tc_tail('delete specific tier')
        assert NetworkUtils.delete_specific_network(network_id) is True, tc_tail('delete specific network')
    except AssertionError as ae:
        pytest.fail(f"Test failed due to AssertionError: {ae}")
        # Handle assertion failure
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
        # Handle other exceptions

def test_run_swagger_workflows():
    test_swagger_add_new_subscriber(setup_env)


