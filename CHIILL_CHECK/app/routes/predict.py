from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
import numpy as np
import os
from app.models import Prediction
from app import db
from app.utils.preprocessing import preprocess_input
from tensorflow.keras.models import load_model  # Import the model loader

# Load the trained ANN model
model_path = os.path.join(os.path.dirname(__file__), '../utils/stress_detection_model.keras')
model = load_model(model_path)  # Initialize the model

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        try:
            # Extract form data
            raw_features = np.array([[
                float(request.form.get('snoring_rate')),
                float(request.form.get('respiratory_rate')),
                float(request.form.get('body_temperature')),
                float(request.form.get('limb_movement')),
                float(request.form.get('blood_oxygen')),
                float(request.form.get('eye_movement')),
                float(request.form.get('sleep_hours')),
                float(request.form.get('heart_rate'))
            ]], dtype=np.float32)

            # Preprocess the input
            processed_features = preprocess_input(raw_features)

            # Make prediction
            prediction = model.predict(processed_features)[0][0]
            stress_status = "Stressed" if prediction > 0.5 else "Not Stressed"

            # Save prediction to the database
            new_prediction = Prediction(
                user_id=current_user.id,
                snoring_rate=raw_features[0][0],
                respiratory_rate=raw_features[0][1],
                body_temperature=raw_features[0][2],
                limb_movement=raw_features[0][3],
                blood_oxygen=raw_features[0][4],
                eye_movement=raw_features[0][5],
                sleep_hours=raw_features[0][6],
                heart_rate=raw_features[0][7],
                result=stress_status
            )
            db.session.add(new_prediction)
            db.session.commit()

            # Redirect to the result page
            return redirect(url_for('result.result'))

        except Exception as e:
            print("❌ Error occurred:", str(e))
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for('predict.predict'))

    return render_template('form.html')