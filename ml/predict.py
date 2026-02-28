import numpy as np
import joblib
import os

# -----------------------------
# Load model and scaler
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "crop_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# -----------------------------
# Prediction function
# -----------------------------
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):

    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)

    return prediction[0]


# -----------------------------
# Test prediction (sample input)
# -----------------------------
if __name__ == "__main__":

    crop = predict_crop(
        N=90,
        P=40,
        K=40,
        temperature=25,
        humidity=80,
        ph=6.5,
        rainfall=200
    )

    print("Recommended Crop:", crop)