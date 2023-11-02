#############################################################################
## Swagger Basic test scenarios ##
#############################################################################
** Test Configuration **
***
Currently the tests acccept following parameters:

   - IP = IP of the VM running Swagger
   - Port = Port of the Swagger UI

#############################################################################
## Swagger E2E Workflow tests ##
#############################################################################
Swagger has below major End 2 End Worfklows:
- Network Management
- Gateway Management
- Apn Management
- Policy Management
- Subscriber Management
- Multiple Subscriber Management

Pre-requisites:
These tests use needs following requirements:
- Installation of orc8r and AGW in one VM
- To install orc8r and AGW in one VM, you can follow the script in below directory
   pmn-systems/agw_orc8r_deploy.sh

** Test Execution host **
Python3 with following packages installed
- pip3
- Following python modules:
  - pytest
  - requests
  
** Execution steps **:
- Clone the repo
   git clone git@github.com:wavelabsai/pmn-systems.git
   * Make sure to select test-Automation branch and clone the code *
- Go to pmn-systems/testing/tests
- Make sure your default python version python3
- Install pytest: sudo pip3 install pytest
- Set the following environment variables:
    - export hostIP='\<IP of swagger host\>'
    - export hostPort='\<Swagger Port\>'
- Examples values 
    - export hostIP='172.16.5.107'
    - export hostPort='9443'

- go to: pmn-systems/testing/tests directory and execute
   below command to run the test cases
  pytest -m swagger_subscriber-v -s (E2E subscriber addition, updation and cleanup) 
  pytest -m swagger_network -v -s (E2E network addtion, updation and cleanup)
  pytest -m swagger_gateway -v -s (E2E gateway addition, updation and cleanup)
  pytest -m swagger_apn -v -s (E2E apn addition, updation and cleanup)
  pytest -m swagger_gateway -v -s (E2E gateway addition, updation and cleanup)
  pytest -m swagger_multiple_subscribers -v -s (E2E multiple subscriber addition)

- Above execution will save the logs and html reports in below directory
  * you can find the logs from here *
  pmn-systems/testing/logs/pytest-logs.txt

  *you can find the html report from here *
  pmn-systems/testing/tests/results/pmn_systems_test_report.html

***
## END Section: Swagger test scenarios  ##
***
**Authors / Maintainers**:

-   **Srinivas Pittala (<srinivas.pittala@wavelabs.ao>)**
-   **Rupa Dangudubiyyam (<rupa.seshaveni@wavelabs.ai>)**


