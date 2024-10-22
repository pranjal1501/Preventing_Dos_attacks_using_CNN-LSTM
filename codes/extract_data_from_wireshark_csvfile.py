import pandas as pd
import os

# Load the CSV file
csv_file_path = r'E:/iot/packet_info_bw_laptopandphone.csv'
data = pd.read_csv(csv_file_path)

# Initialize counters and variables
src_bytes = 0
dst_bytes = 0
total_connections = 0
syn_errors = 0
rej_errors = 0

# Iterate through the rows of the DataFrame
for index, row in data.iterrows():
    src_ip = row['Source']
    dst_ip = row['Destination']
    packet_length = row['Length']

    # Count bytes
    src_bytes += packet_length
    dst_bytes += packet_length  # Modify this logic if you have specific conditions for destination bytes

    # Count total connections
    total_connections += 1

    # Check for SYN errors
    if 'SYN' in row['Info']:
        syn_errors += 1
    
    # Check for REJ errors
    if 'RST' in row['Info']:
        rej_errors += 1

# Calculate rates
serror_rate = syn_errors / total_connections if total_connections > 0 else 0
rerror_rate = rej_errors / total_connections if total_connections > 0 else 0

# Prepare data to save
feature_data = {
    'src_bytes': [src_bytes],
    'dst_bytes': [dst_bytes],
    'syn_errors': [syn_errors],
    'rej_errors': [rej_errors],
    'serror_rate': [serror_rate],
    'rerror_rate': [rerror_rate]
}

# Create a DataFrame
features_df = pd.DataFrame(feature_data)

# Ensure output directory exists, and save to a new location (for example, Documents folder)
output_directory = r'E:/iot/'
output_file_path = os.path.join(output_directory, 'output_packet_info.csv')

try:
    features_df.to_csv(output_file_path, index=False)
    print(f"Extracted features saved to {output_file_path}")
except PermissionError:
    print(f"Permission denied: Unable to write to {output_file_path}. Check the directory permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
