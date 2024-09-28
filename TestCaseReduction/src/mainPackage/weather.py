import pandas as pd
import os
import sys
sys.path.append(os.path.abspath("src"))

from reportGen import run_tests_and_report
from mainPackage import DataHandle      

def get_columns(df):
    return df.columns

def get_min_temp(df):
    return df['MinTemp'].min()

def get_max_temp(df):
    return df['MaxTemp'].max()

def avg_temp(df):
    combined_average = (df['MinTemp'] + df['MaxTemp']).mean()
    return combined_average

def calculate_average(row):
    selected_columns = [
        'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
        'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
        'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
        'Temp9am', 'Temp3pm'
    ]
    total = sum([row[col] for col in selected_columns])
    return total / len(selected_columns)

def read_data():
    df = pd.read_csv('src/resources/weather.csv')

    return df

if __name__ == "__main__":
    df = read_data()
    print(df.head())
    df = DataHandle.handlingNullData(df)
    print(get_columns(df))
    print(get_min_temp(df))
    print(get_max_temp(df))
    print(avg_temp(df))
    df['average'] = df.apply(calculate_average, axis=1)
    print(df['average'].head())