import sys
import os
import pandas as pd
# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath("src"))

# Now you can import functions from weather.py
from mainPackage import weather
from testWeather import TestWeatherFunctions
from reportGen import run_tests_and_report
from mainPackage import DataHandle
def main():
    # Use functions from weather.py
    df = weather.read_data()

    run_tests_and_report()

if __name__ == "__main__":
    main()
