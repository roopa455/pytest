import unittest
import HtmlTestRunner


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)

    def test_another_example(self):
        self.assertEqual(3 * 4, 12)


if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTest))

    # Define the output file path for the HTML report
    report_path = 'test_report.html'

    # Open the report file in write mode
    with open(report_path, 'wb') as report_file:
        # Create an HTMLTestRunner instance
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=report_file,
            title='Test Report',
            description='This is a sample test report'
        )

        # Run the test suite
        runner.run(suite)
