Preventing DoS Attacks Using CNN-LSTM
This project aims to detect Denial-of-Service (DoS) attacks on Healthcare IoT (H-IoT) devices in real-time using a hybrid CNN-LSTM model. The system processes network traffic features for fast detection on edge devices, with further validation in the cloud to ensure accuracy.

Key Features:
Real-time DoS Detection: CNN extracts features, LSTM analyzes traffic over time.
Cloud Validation: Verifies flagged traffic to reduce false positives.
Secure Communication: Uses AES encryption for transmitting suspicious data.

How to Test:
Use Wireshark to capture network packets.
Run the trained CNN-LSTM model to analyze the captured data.

Folders:
codes/: Contains scripts for preprocessing dataset,analysis and visualization.
analysis/: Holds analysis scripts for performance metrics.
plots/: Includes visualizations of all attributes.

DATASET LINK:  https://www.kaggle.com/datasets/hassan06/nslkdd/data
SOURCE: Kaggle
File used : KDDTain+

