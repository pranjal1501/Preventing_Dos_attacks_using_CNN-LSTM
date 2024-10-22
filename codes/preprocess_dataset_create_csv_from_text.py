import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load the data
data = pd.read_csv("E:/iot/archive/KDDTrain+.txt", header=None)

# Columns based on the description of the dataset
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 
           'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 
           'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate', 'attack', 'last_flag']

# Assign column names
data.columns = columns

# Convert categorical columns into numerical values
label_encoders = {}
for col in ['protocol_type', 'service', 'flag']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Map the 'attack' column to binary classification: 0 for 'normal', 1 for 'DoS attacks'
# List of known DoS attacks (from the KDD dataset description)
dos_attacks = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop']

# Apply the mapping
data['attack'] = data['attack'].apply(lambda x: 1 if x in dos_attacks else 0)

# Normalize numerical features
scaler = MinMaxScaler()
numerical_columns = data.columns.difference(['protocol_type', 'service', 'flag', 'attack'])
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Save the preprocessed and classified data to a CSV file
output_file_path = "C:/Users/pranj/Downloads/preprocessed_KDDTest_data_binary.csv"
data.to_csv(output_file_path, index=False)

print(f"Preprocessed and classified data saved to {output_file_path}")
