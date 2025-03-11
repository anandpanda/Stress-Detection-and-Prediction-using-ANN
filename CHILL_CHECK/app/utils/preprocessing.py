import pickle
import pandas as pd
import os

current_dir = os.path.dirname(__file__)
scaler_path = os.path.join(current_dir, "minmax_scaler.pkl")

with open(scaler_path, "rb") as f:
    minmax_scaler = pickle.load(f)

def preprocess_input(raw_features):
    feature_columns = ["Snoring Rate", "Respiratory Rate", "Body Temperature", 
                       "Limb Movement", "Blood Oxygen", "Eye Movement", 
                       "Sleep Hours", "Heart Rate"]
    raw_features_df = pd.DataFrame(raw_features, columns=feature_columns)
    processed_features = minmax_scaler.transform(raw_features_df)
    return processed_features