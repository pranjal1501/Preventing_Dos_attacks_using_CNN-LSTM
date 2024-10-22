from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

# Load the NSL-KDD dataset
data = pd.read_csv("E:/iot/archive/KDDTrain+.txt", header=None)

# Assign appropriate column names
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
           'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 
           'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate', 'attack', 'last_flag']

data.columns = columns

# List of features for normalization
selected_features = ['serror_rate', 'srv_serror_rate', 'src_bytes', 'dst_bytes', 'rerror_rate', 'srv_rerror_rate', 
                     'count', 'srv_count', 'same_srv_rate']

# Normalize the selected features using MinMaxScaler
scaler = MinMaxScaler()
data[selected_features] = scaler.fit_transform(data[selected_features])

# Convert 'attack' column to binary (1 for DoS, 0 for normal)
dos_attacks = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm']
data['attack_binary'] = data['attack'].apply(lambda x: 1 if x in dos_attacks else 0)

# Function to calculate mean for a random sample of 100 data points
def calculate_means():
    mean_values = {}
    for feature in selected_features:
        # Normal (100 random samples)
        normal_sample = data[data['attack_binary'] == 0].sample(10000, random_state=42)
        mean_normal = np.mean(normal_sample[feature])
        
        # DoS Attack (100 random samples)
        dos_sample = data[data['attack_binary'] == 1].sample(10000, random_state=42)
        mean_dos = np.mean(dos_sample[feature])
        
        mean_values[feature] = (mean_normal, mean_dos)
    
    # Convert to DataFrame for readability
    mean_df = pd.DataFrame(mean_values, index=['Normal (10000 Sample)', 'DoS Attack (10000 Sample)']).T
    return mean_df

# Calculate and output the means
mean_df = calculate_means()
print(mean_df)

# Save the results to a CSV file for further review
mean_df.to_csv("mean_analysis_normalized.csv")
