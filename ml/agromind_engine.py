import numpy as np
import joblib
import os
from ml.soil_diagnosis import diagnose_soil

# -----------------------------
# Load model and scaler
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "crop_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# -----------------------------
# Main AgroMind function
# -----------------------------
def agromind_recommend(N, P, K, temperature, humidity, ph, rainfall):

    # Prepare features
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    features_scaled = scaler.transform(features)

    # Crop prediction
    crop = model.predict(features_scaled)[0]

    # Soil diagnosis
    soil_report = diagnose_soil(crop, N, P, K)

    return {
        "recommended_crop": crop,
        "soil_health_report": soil_report
    }


# -----------------------------
# Test AgroMind system
# -----------------------------
if __name__ == "__main__":

    result = agromind_recommend(
        N=40,
        P=50,
        K=45,
        temperature=25,
        humidity=80,
        ph=6.5,
        rainfall=200
    )

    print("\nAGROMIND RESULT")
    print("-------------------")
    print("Recommended Crop:", result["recommended_crop"])
    print("Soil Report:", result["soil_health_report"])