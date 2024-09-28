import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

def reduce_test_cases(input_file, output_file, n_clusters):
    df = pd.read_csv(input_file)

    df_numeric = df.drop(columns=['Test Case', 'Input', 'Adequacy_Label'])

    df_encoded = pd.get_dummies(df_numeric)

    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=100)
        df['cluster'] = kmeans.fit_predict(df_encoded)
    except Exception as e:
        print("Error occurred during clustering:", e)
        return

    reduced_test_cases = df.groupby('cluster').first().reset_index(drop=True)

    reduced_test_cases.to_csv(output_file, index=False)

def main():
    input_file = './src/resources/final_test_dataset_RF.csv'
    output_file = './src/resources/reduced_data.csv'
    n_clusters = 10

    reduce_test_cases(input_file, output_file, n_clusters)

if __name__ == "__main__":
    main()
