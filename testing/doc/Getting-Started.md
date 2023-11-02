# Prerequisites
=================
Before proceeding with script execution, make sure the following prerequisites are satisfied:

1. A computer with the necessary software and dependencies installed. This includes python and pycharm IDE software.
Pre installation of the following python modules are required:

* requests
* yaml
* HTTPDigestAuth
* json
* urllib3
* datetime
* time
* unittest
* logging
* sys
* PyQt6.QtCore 
* PyQt6.QtWidgets
* PyQt6.QtGui
* os
* HTMLTestRunner

[Note: Pycharm will auto install the required modules after a git clone.(step2).
also, it can be manually installed using pycharm Python packages tab, if required.

2. Access to the relevant source code repository or file storage location. 
This will be stored in the main github remote repo ```https://github.com/wavelabsai/pmn-systems```



#### Steps to execute scripts

Cloning of remote repository to the local machine is required before starting the script execution.


Open pycharm terminal and execute the following command to clone a remote repository to local machine using 'Git':

```git clone https://github.com/wavelabsai/pmn-systems```


#### Directory structure


The automation framework contains the following three main directories

- Backend
- Frontend
- Reports

Backend directory contains all the necessary config. files, certificate files, yaml files, json files etc. 
User defined parameters are present in backend/config/user-config.yaml
Frontend directory contains all the test scripts grouped module wise, such as network, APN, subscriber db, policy db etc.
Reports directory contains log files by their execution date and time and html test reports. Log files and reports are auto generated
after each execution.

#### Steps to execute a single test script


Open pycharm terminal

Navigate to the file folder and run the command. For example:

``cd \frontend\test``

then, run ``py <test-script.py>``

ex:

``py test_API_M1_LTE_APN_TC0001_Get_APN.py``


#### Steps to execute all the  scripts together in a batch

To run all test scripts in batch, go to frontend directory and run the main.py file.

`cd frontend
`
`py main.py`
**Note**: prior to running the batch file, all test scripts are to be placed in frontend/test folder, with their title starting with 'test_' keyword

#### Steps to run a specific module
If you want to run a specific module, say APN module, Change the module to pattern = '`test_API_{module}_*.py`' on on line #15 of the 'main' python file
and run the main.py file using py main.py

i.e.,
`files = loader.discover(start_dir=folder, pattern='test_API_M1_LTE_APN_*.py')
`
to run all scripts in network module:

`files = loader.discover(start_dir=folder, pattern='test_API_M1_LTE_Network_*.py')
`
#### Monitor the execution and viewing logs
While the script is running, monitor the console output and logs for any errors or unexpected behavior. (In the batch file, the `main.py` file will be running in the backend.
It will show the following log in the terminal once completed: `Html test report generated`)
The reports folder will contain a 'logs' sub folder that contains all the execution logs with the date and time of execution
and a 'html-reports' sub folder that contains a consolidated pass/fail html report (only in case of a batch run)
The html report can be opened and viewed using a browser.

