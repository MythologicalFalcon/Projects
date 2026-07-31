import os
import pandas as pd
from sklearn.neighbors import NearestNeighbors

def reduce_test_cases(input_file, output_file, n_neighbors):
    df = pd.read_csv(input_file)

    numeric_cols = df.select_dtypes(include=['number']).columns
    non_numeric_rows = df[~df[numeric_cols].apply(pd.to_numeric, errors='coerce').notnull().all(axis=1)]

    if not non_numeric_rows.empty:
        print("Error: Non-numeric values detected in the dataset.")
        print("Rows with non-numeric values:")
        print(non_numeric_rows)
        return

    df.dropna(inplace=True)

    numeric_features = df.drop(columns=['Test Case', 'Input', 'Adequacy_Label'])

    try:
        knn = NearestNeighbors(n_neighbors=n_neighbors)
        knn.fit(numeric_features)
        distances, indices = knn.kneighbors(numeric_features)
    except Exception as e:
        print("Error occurred during KNN:", e)
        return

    # Column 0 of kneighbors() is the point itself when the model is fitted and queried
    # on the same data, so indices[:, 0] is just the original row order and reduces
    # nothing. Walk the rows instead and keep a case only if none of its neighbours has
    # already been kept, which is what drops the near-duplicates.
    kept = []
    covered = set()
    for row, neighbours in enumerate(indices):
        if row in covered:
            continue
        kept.append(row)
        covered.update(neighbours.tolist())

    reduced_test_cases = df.iloc[kept].reset_index(drop=True)
    print(f"Reduced {len(df)} test cases to {len(reduced_test_cases)}.")

    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True) 
    reduced_test_cases.to_csv(output_file, index=False)

    print("Reduced test cases saved to", output_file)

def main():
    input_file = './src/resources/final_test_dataset_RF.csv'
    output_file = './src/resources/reduced_data.csv'
    n_neighbors = 5 

    reduce_test_cases(input_file, output_file, n_neighbors)

if __name__ == "__main__":
    main()
