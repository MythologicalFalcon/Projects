import coverage
import unittest
import time
import csv
import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath("src"))

from mainPackage import weather
from testWeather import TestWeatherFunctions

def run_tests_and_report():
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Record the start time
    start_time = time.time()

    # Run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeatherFunctions)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Record the end time
    end_time = time.time()

    # Stop coverage and generate report
    cov.stop()
    cov.save()

    # Calculate execution time
    execution_time = end_time - start_time

    # Save report to CSV
    with open('test_report.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Test Name', 'Outcome', 'Execution Time', 'Coverage'])

        for test in suite:
            test_name = test.id().split('.')[-1] if test else 'Unknown'
            outcome = "Pass" if test_name not in test_result.failures else "Fail"
            writer.writerow([test_name, outcome, execution_time, ''])

if __name__ == "__main__":
    run_tests_and_report()
