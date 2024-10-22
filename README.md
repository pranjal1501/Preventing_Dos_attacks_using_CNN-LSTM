Preventing DoS Attacks Using CNN-LSTM
This project aims to detect Denial-of-Service (DoS) attacks on Healthcare IoT (H-IoT) devices in real-time using a hybrid CNN-LSTM model. The system processes network traffic features for fast detection on edge devices, with further validation in the cloud to ensure accuracy.

Key Features:
Real-time DoS Detection: CNN extracts features, LSTM analyzes traffic over time.
Cloud Validation: Verifies flagged traffic to reduce false positives.
Secure Communication: Uses AES encryption for transmitting suspicious data.

How to Test:
Use Wireshark to capture network packets.
Run the trained CNN-LSTM model to analyze the captured data.

Folder Structure
codes/: Contains the Python scripts for training, preprocessing, and testing the model.
dataset/: Includes sample datasets in text and CSV formats.
analysis/: Scripts for feature extraction, calculating mean values, and plotting traffic patterns.

Main Scripts
preprocess_dataset_create_csv_from_text: Converts raw text data to CSV format and applies MinMax normalization for 39 attributes to standardize data.
extract_data_from_wireshark_csvfile: Prepares Wireshark-captured packet data by formatting it to align with the training dataset.
mean_analysis: Computes the mean of specific attributes (customizable) over random data points for statistical analysis.
plot_graphs: Visualizes selected traffic attributes, allowing for the comparison between normal and attack traffic.

DATASET LINK:  https://www.kaggle.com/datasets/hassan06/nslkdd/data
SOURCE: Kaggle
File used : KDDTain+

