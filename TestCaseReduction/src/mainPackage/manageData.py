import pandas as pd
import ast
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder 

def is_preprocessed(data):
    # Check if the data has the correct number of columns
    expected_columns = [
        "Test Case",
        "Input",
        "Maximum Subarray Sum",
        "Branch_Coverage",
        "Statement_Coverage",
        "Function_Coverage",
        "Execution_Time",
        "Adequacy_Score",
        "Adequacy_Label"
    ]
    if len(data[0]) != len(expected_columns):
        return False

    # Check if all rows have the correct number of elements
    for row in data:
        if len(row) != len(expected_columns):
            return False

    # Check if the "Input" column contains lists of integers
    for row in data:
        try:
            input_list = ast.literal_eval(row[1])
            if not isinstance(input_list, list):
                return False
            for item in input_list:
                if not isinstance(item, int):
                    return False
        except (SyntaxError, ValueError):
            return False

    # Check if other columns have valid data types or formats
    for row in data:
        try:
            float(row[2])  # Maximum Subarray Sum
            float(row[3])  # Branch_Coverage
            float(row[4])  # Statement_Coverage
            if not row[5].endswith('%'):  # Function_Coverage
                return False
            float(row[6])  # Execution_Time
            float(row[7])  # Adequacy_Score
            if row[8] not in ['low', 'mid']:  # Adequacy_Label
                return False
        except ValueError:
            return False

    return True


def randomForestClassifier(df_train, df_test):
    # Preprocess the training data
    df_train['Function_Coverage'] = df_train['Function_Coverage'].str.rstrip('%').astype(float) / 100.0
    df_train['Maximum Subarray Sum'] = pd.to_numeric(df_train['Maximum Subarray Sum'], errors='coerce')
    df_train['Execution_Time'] = pd.to_numeric(df_train['Execution_Time'], errors='coerce')
    df_train = df_train.dropna()
    df_train['Input'] = df_train['Input'].apply(lambda x: len(eval(x)))
    label_encoder = LabelEncoder()
    df_train['Adequacy_Label'] = label_encoder.fit_transform(df_train['Adequacy_Label'])

    # Select numeric columns for training
    numeric_columns = ['Input', 'Maximum Subarray Sum', 'Branch_Coverage', 'Statement_Coverage',
                       'Function_Coverage', 'Execution_Time', 'Adequacy_Score', 'Adequacy_Label']
    df_train = df_train[numeric_columns].astype(float)

    # Split the training data into features (X) and target labels (y)
    X_train = df_train.drop('Adequacy_Label', axis=1)
    y_train = df_train['Adequacy_Label']

    # Train a Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust the parameters
    rf_classifier.fit(X_train, y_train)

    # Preprocess the test data
    df_test['Function_Coverage'] = df_test['Function_Coverage'].str.rstrip('%').astype(float) / 100.0
    df_test['Maximum Subarray Sum'] = pd.to_numeric(df_test['Maximum Subarray Sum'], errors='coerce')
    df_test['Execution_Time'] = pd.to_numeric(df_test['Execution_Time'], errors='coerce')
    df_test = df_test.dropna()
    df_test['Input'] = df_test['Input'].apply(lambda x: len(eval(x)))
    df_test['Adequacy_Label'] = label_encoder.transform(df_test['Adequacy_Label'])  # Use transform instead of fit_transform

    # Select numeric columns for testing
    df_test = df_test[numeric_columns].astype(float)

    # Split the test data into features (X_test) and target labels (y_test)
    X_test = df_test.drop('Adequacy_Label', axis=1)
    y_test = df_test['Adequacy_Label']

    # Predict labels for the test data
    y_pred = rf_classifier.predict(X_test)

    # Calculate accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Return predicted labels for the test data
    print( y_pred)






df = pd.read_csv('./src/resources/final_test_dataset_RF.csv')
df1 = pd.read_csv('./src/resources/sampletestData.csv')

data = df.values.tolist()

if is_preprocessed(data):
    print("The data is preprocessed.")
    randomForestClassifier(df)
else:
    # Call the preprocessing function
    print("The data is not preprocessed.")
    randomForestClassifier(df,df1)


