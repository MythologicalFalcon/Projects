import sys
import os
import pandas as pd
import unittest

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath("src"))
from mainPackage import weather

class TestWeatherFunctions(unittest.TestCase):

    def setUp(self):
        # Define a sample DataFrame for testing
        data = {
            'MinTemp': [8, 14, 13.7, 13.3, 7.6, 6.2, 6.1, 8.3],
            'MaxTemp': [24.3, 26.9, 23.4, 15.5, 16.1, 16.9, 18.2, 17],
            'Rainfall': [0, 3.6, 3.6, 39.8, 2.8, 0, 0.2, 0],
            'Evaporation': [3.4, 4.4, 5.8, 7.2, 5.6, 5.8, 4.2, 5.6],
            'Sunshine': [6.3, 9.7, 3.3, 9.1, 10.6, 8.2, 8.4, 4.6],
            'WindGustSpeed': [30, 39, 85, 54, 50, 44, 43, 41],
            'WindSpeed9am': [6, 4, 6, 30, 20, 20, 19, 11],
            'WindSpeed3pm': [20, 17, 6, 24, 28, 24, 26, 24],
            'Humidity9am': [68, 80, 82, 62, 68, 70, 63, 65],
            'Humidity3pm': [29, 36, 69, 56, 49, 57, 47, 57],
            'Pressure9am': [1019.7, 1012.4, 1009.5, 1005.5, 1018.3, 1023.8, 1024.6, 1026.2],
            'Pressure3pm': [1015, 1008.4, 1007.2, 1007, 1018.5, 1021.7, 1022.2, 1024.2],
            'Cloud9am': [7, 5, 8, 2, 7, 7, 4, 6],
            'Cloud3pm': [7, 3, 7, 7, 7, 5, 6, 7],
            'Temp9am': [14.4, 17.5, 15.4, 13.5, 11.1, 10.9, 12.4, 12.1],
            'Temp3pm': [23.6, 25.7, 20.2, 14.1, 15.4, 14.8, 17.3, 15.5],
            'RainToday': ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No'],
            'RISK_MM': [3.6, 3.6, 39.8, 2.8, 0, 0.2, 0, 0],
            'RainTomorrow': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No']
        }
        self.df = pd.DataFrame(data)

    def test_getMinTemp(self):
        """Test case for getting minimum temperature."""
        self.assertIsNotNone(weather.get_min_temp(self.df))

    def test_getMaxTemp(self):
        """Test case for getting maximum temperature."""
        self.assertIsNotNone(weather.get_max_temp(self.df))

    def test_avgTemp(self):
        """Test case for calculating average temperature."""
        self.assertIsNotNone(weather.avg_temp(self.df))

    def test_calculate_average_all_ones(self):
        """Test case for calculating average of all ones."""
        row = pd.Series(1, index=self.df.columns)
        self.assertIsNotNone(weather.calculate_average(row))

    def test_calculate_average_all_zero(self):
        """Test case for calculating average of all zeros."""
        row = pd.Series(0, index=self.df.columns)
        self.assertIsNotNone(weather.calculate_average(row))

    # Add more test cases for calculate_average function covering different scenarios


if __name__ == '__main__':
    unittest.main()
