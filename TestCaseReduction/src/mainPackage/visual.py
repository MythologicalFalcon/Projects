import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, Dropdown
from IPython.display import display

def plot_bar_graph(test_case_id, original_df, reduced_df):
    original_subset = original_df[original_df['Test Case'] == test_case_id]
    reduced_subset = reduced_df[reduced_df['Test Case'] == test_case_id]

    original_numeric_df = original_subset.select_dtypes(include='number')
    reduced_numeric_df = reduced_subset.select_dtypes(include='number')

    original_means = original_numeric_df.mean()
    reduced_means = reduced_numeric_df.mean()

    fig, ax = plt.subplots(figsize=(12, 6))
    bar_width = 0.35
    index = np.arange(len(original_means))

    original_bars = ax.bar(index, original_means, bar_width, label='Original')
    reduced_bars = ax.bar(index + bar_width, reduced_means, bar_width, label='Reduced')

    ax.set_xlabel('Numeric Columns')
    ax.set_ylabel('Mean Value')
    ax.set_title(f'Mean Values for Test Case ID {test_case_id}')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(original_means.index)
    ax.legend()

    plt.show()

def main():
    original_file = './src/resources/final_test_dataset_RF.csv' 
    reduced_file = './src/resources/reduced_data.csv'   

    
    original_df = pd.read_csv(original_file)
    reduced_df = pd.read_csv(reduced_file)

    
    reduced_test_case_ids = reduced_df['Test Case'].unique()

    
    test_case_dropdown = Dropdown(options=reduced_test_case_ids, description='Test Case ID:')

    
    def update_plot(test_case_id):
        plot_bar_graph(test_case_id, original_df, reduced_df)

    interact(update_plot, test_case_id=test_case_dropdown)

if __name__ == "__main__":
    main()
