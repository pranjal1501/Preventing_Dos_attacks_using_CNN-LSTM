import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the preprocessed data from the provided CSV file path
file_path = "E:/iot/preprocessed_KDDTest_data_binary.csv"
data = pd.read_csv(file_path)

# Set the directory to save the plots in the current working directory
output_dir = os.path.join(os.getcwd(), 'plots')
os.makedirs(output_dir, exist_ok=True)

# Set a random seed for reproducibility
np.random.seed(42)

# Separate data into normal and DoS attack conditions (1000 samples each)
normal_data = data[data['attack'] == 0].sample(1000, random_state=42)
dos_data = data[data['attack'] == 1].sample(1000, random_state=42)

# Exclude non-numerical and target columns
columns_to_plot = data.columns.difference(['protocol_type', 'service', 'flag', 'attack'])

# Set the plotting style
sns.set(style='whitegrid')

# Create separate plots for each feature and save them
for column in columns_to_plot:
    plt.figure(figsize=(8, 4))
    
    # Plot the distribution of the feature for normal and DoS attack conditions
    sns.kdeplot(normal_data[column], label='Normal', color='blue', fill=True)
    sns.kdeplot(dos_data[column], label='DoS Attack', color='red', fill=True)
    
    # Title and labels
    plt.title(f'Distribution of {column} - Normal vs DoS Attack')
    plt.xlabel(column)
    plt.ylabel('Density')
    
    # Save the plot as a PNG file
    plot_file_path = os.path.join(output_dir, f'{column}_distribution.png')
    plt.savefig(plot_file_path)
    
    # Close the plot to free memory
    plt.close()

print(f"Plots saved to {output_dir}")
