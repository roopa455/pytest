import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 1)[0]
sys.path.append(root_dir)
from backend.configs.package import *

# Define your test cases here


folder = 'test'
loader = unittest.TestLoader()
runner = unittest.TextTestRunner()

files = loader.discover(start_dir=folder, pattern='test_*.py')


# Get the current date and time
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a report file
report_dir = os.path.join(os.getcwd(), "../reports/html-reports")
os.makedirs(report_dir, exist_ok=True)
report_file = os.path.join(report_dir, f"html_report_{now}.html")

# Create a HTMLTestRunner and run the test suite
with open(report_file, "w") as f:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title="Juniper Test Report",
        description="This report displays the actual file name, Functions, and status of the test cases."
                    "",
    )
    runner.run(files)


# Print the path to the report file
print(f"Html test report generated: {report_file}")
