import tensorflow as tf
import pickle
import numpy as np

# Step 1: Load the saved model and scaler
model = tf.keras.models.load_model('D:\Stress Detection and Prediction using ANN\Model\stress_detection_model.keras')
with open("D:\Stress Detection and Prediction using ANN\Model\minmax_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Step 2: Prepare new data
new_data = np.array([
    [95,20,91,18,91,99,2,70]
])

# Normalize the new data
new_data_normalized = scaler.transform(new_data)
print("Normalized : ", new_data_normalized)

# Step 3: Make predictions
predictions = model.predict(new_data_normalized)
predicted_classes = (predictions > 0.5).astype(int)

# Step 4: Interpret the results
print("Predicted Probabilities:", predictions)
print("Predicted Classes:", predicted_classes)