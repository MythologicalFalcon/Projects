import pandas as pd

# Load the dataset
data = pd.read_csv('dataset_with_adequacy_score.csv')

# Determine quartiles of the adequacy scores
quartiles = data['Adequacy_Score'].quantile([0.25, 0.5, 0.75])

# Define labels based on quartiles
low_threshold = quartiles[0.25]
high_threshold = quartiles[0.75]

# Labeling function
def label_adequacy_score(score):
    if score < low_threshold:
        return 'low'
    elif low_threshold <= score < high_threshold:
        return 'mid'
    else:
        return 'high'

# Apply labeling function to adequacy scores
data['Adequacy_Label'] = data['Adequacy_Score'].apply(label_adequacy_score)

data.to_csv('labeled_dataset.csv', index=False)
