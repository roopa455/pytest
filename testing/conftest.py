import sys, random
import os
import configparser
import time
import logging
import threading     # In-build modules
import pytest
import globals.globals as gbl       # Import our own modules
from datetime import datetime
import re
from py.xml import html
# getting user name
from pwd import getpwuid
from os import getuid
# getting python version
from platform import python_version
from swagger_utilities.swagger_utils import Swagger_Utils
swagger_utils = Swagger_Utils()
config = configparser.RawConfigParser()

_logger = logging.getLogger('ConfTest')
load_config_file = "../config_file.ini"

@pytest.fixture(scope="session")
def random_values():
    random_value = random.randint(1, 1000)
    global network_id, name, tier_id, apn_name, policy_id, subscriber_id
    network_id = "lte_network_" + str(random_value)
    name = "lte_" + str(random_value)
    tier_id = "test_tier_" + str(random_value)
    gateway_id = "test_gateway_" + str(random_value)
    apn_name = "test_apn_" + str(random_value)
    policy_id = "test_policy_" + str(random_value)
    subscriber_id = "IMSI001010000000" + str(random_value)
    return network_id, name, tier_id, gateway_id, apn_name, policy_id, subscriber_id

@pytest.fixture()
def setup_env(random_values):
    network_id, name, tier_id, gateway_id, apn_name, policy_id, subscriber_id = random_values
    swagger_utils.prCyan(f'Setting up test environment')
    return network_id, name, tier_id, gateway_id, apn_name, policy_id, subscriber_id
    #yield "setup_env"

def pytest_html_report_title(report):
	''' modifying the title of html report'''
	report.title = "Swagger API Test Scenarios"

def pytest_configure(config):
	''' modifying the table pytest environment'''

	username = getpwuid(getuid())[0]

	py_version = python_version()
	# overwriting old parameters with new parameters
	config._metadata = {
		"user_name": username,
		"python_version": py_version,
	}

def pytest_html_results_table_header(cells):
	''' meta programming to modify header of the result'''

	# removing old table headers
	del cells[1]
	# adding new headers
	cells.insert(0, html.th('Time', class_='sortable time', col='time'))
	cells.insert(1, html.th('Tag'))
	cells.insert(2, html.th('Testcase'))
	cells.pop()

def pytest_html_results_table_row(report, cells):
	''' orienting the data gotten from pytest_runtest_makereport
	and sending it as row to the result '''
	del cells[1]
	cells.insert(0, html.td(datetime.utcnow(), class_='col-time'))
	cells.insert(1, html.td(report.tag))
	cells.insert(2, html.td(report.testcase))
	cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
	'''data from the output of pytest gets processed here
	and are passed to pytest_html_results_table_row'''
	outcome = yield
	# this is the output that is seen end of test case
	report = outcome.get_result()
	# taking doc string of the string
	testcase = str(item.function.__doc__)
	# name of the functton
	c = str(item.function.__name__)[5:]

	report.testcase = f"{c} [{testcase}]"
	# taking input args
	# example:
	# report.nodeid = 'tests/test_case.py::test_min[input0-1]'
	# data = re.split(r"\[|\]", 'tests/test_case.py::test_min[input0-1]')
	# => ['tests/test_case.py::test_min', 'input0-1', '']
	report.tag = re.split(r"\[|\]", report.nodeid)[-1]

@pytest.fixture(scope="session")
def run_setup(request, pytestconfig):
    
    #To set the cmd line argument values to the global variables and set the cookie value
    
    _logger.info('\nDoing common setup once for all tests in this session...')
    if os.path.isfile(load_config_file) is False:
        _logger.error('Missing config_file.ini, please make sure there is one.')
        return False
    config.read(load_config_file)
    host_ip = config.get('Deployment_Values', 'host_ip')  # Get amcop_deployment_ip setting
    host_port = config.get('Deployment_Values', 'host_port')  # Get middle_end_port setting
    if pytestconfig.getoption("ip") is not None:
        gbl.host_ip = pytestconfig.getoption("ip")
        _logger.info("The deployment ip provided from cmd line is  {}".format(gbl.host_ip))
    elif pytestconfig.getoption("ip") is None and host_ip is not None:
        gbl.host_ip = host_ip
        _logger.info("The deployment from config.ini is  {}".format(gbl.host_ip))
    else:
        _logger.error("Provide the deployment ip from cmd line or set it in the config.ini file")
        return False

    swagger_utils.host_ip = gbl.host_ip
    
    def teardown():
       _logger.info("Collecting env details in teardown.")

    request.addfinalizer(teardown)

def pytest_addoption(parser):
    """
    Add the cmd line arguments need to be supported
    """
    parser.addoption(
        "--ip",
        action="store",
        default=None,
        help="deployment host ip"
    )


