# 🌱 AgroMind — AI-Powered Smart Agriculture Assistant

AgroMind is an **AI-powered smart agriculture application** designed to help farmers make better crop and soil-related decisions using machine learning.

The system analyzes **soil and environmental parameters** and provides intelligent crop recommendations. It also includes a backend API that connects the machine learning models with the application interface.

The project aims to make agricultural decision-making **simpler, faster, and more accessible** by using data-driven recommendations.

---

## 🚀 Key Features

### 🌾 Crop Recommendation

AgroMind recommends a suitable crop based on important agricultural and soil parameters such as:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

The machine learning model analyzes these parameters and predicts the most suitable crop.

### 🧪 Soil Analysis

The application uses soil-related parameters to help understand whether the given conditions are appropriate for crop cultivation.

### 🤖 Machine Learning

The project uses a machine learning pipeline that includes:

* Data preprocessing
* Outlier detection
* Feature scaling
* Train-test splitting
* Model training
* Model persistence

The trained preprocessing components are saved so that the same transformations can be applied during prediction.

### ⚡ FastAPI Backend

AgroMind uses **FastAPI** to provide a backend API for communicating with the machine learning engine.

FastAPI provides:

* High-performance API endpoints
* Automatic API documentation
* Easy integration with the frontend
* Structured request and response handling

Interactive API documentation is available through:

```text
http://127.0.0.1:8000/docs
```

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │      User / Farmer   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Frontend       │
                    │   User Input / UI    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │      Backend         │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
          ┌──────────────────┐   ┌──────────────────┐
          │ AgroMind ML      │   │ Soil Diagnosis   │
          │ Engine           │   │ Module           │
          └────────┬─────────┘   └────────┬─────────┘
                   │                      │
                   └──────────┬───────────┘
                              ▼
                    ┌──────────────────────┐
                    │  Prediction /        │
                    │  Recommendation      │
                    └──────────────────────┘
```

---

## 📂 Project Structure

```text
AgroMind/
│
├── backend/
│   ├── main.py
│   └── ...
│
├── frontend/
│   └── ...
│
├── ml/
│   ├── agromind_engine.py
│   ├── soil_diagnosis.py
│   └── ...
│
├── data/
│   └── Crop_recommendation.csv
│
├── models/
│   └── scaler.pkl
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset

The project uses the **Crop Recommendation Dataset**.

### Dataset Information

| Property       | Details             |
| -------------- | ------------------- |
| Dataset        | Crop Recommendation |
| Rows           | 2,200               |
| Columns        | 8                   |
| Missing Values | None                |

### Features

The dataset contains the following attributes:

| Feature       | Description                |
| ------------- | -------------------------- |
| `N`           | Nitrogen content in soil   |
| `P`           | Phosphorus content in soil |
| `K`           | Potassium content in soil  |
| `temperature` | Temperature                |
| `humidity`    | Humidity                   |
| `ph`          | Soil pH                    |
| `rainfall`    | Rainfall                   |
| `label`       | Recommended crop           |

Dataset location:

```text
data/Crop_recommendation.csv
```

---

# 🧠 Machine Learning Pipeline

The machine learning workflow follows these major steps:

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Outlier Detection
   ↓
IQR-based Outlier Removal
   ↓
Feature Selection
   ↓
StandardScaler
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Preprocessing / Model
   ↓
Prediction
```

## 1. Data Preprocessing

The dataset is checked and prepared before training.

### Outlier Removal

The project uses the **Interquartile Range (IQR)** technique to identify and handle extreme values.

The IQR is calculated as:

```text
IQR = Q3 - Q1
```

Values outside the acceptable range are treated as potential outliers.

### Feature Scaling

`StandardScaler` is used to normalize numerical features.

This helps machine learning algorithms work effectively when features have different numerical ranges.

The trained scaler is saved as:

```text
models/scaler.pkl
```

### Train-Test Split

The dataset is divided into training and testing data using an **80/20 split**.

A fixed `random_state=42` is used to make the experiment reproducible.

---

# 🐍 Technology Stack

## Programming Language

* Python

## Machine Learning

* Pandas
* NumPy
* Scikit-learn
* StandardScaler
* Machine Learning Classification

## Backend

* FastAPI
* Uvicorn
* Python

## Frontend

* Frontend application connected to the FastAPI backend

## Development Tools

* Visual Studio Code
* Python Virtual Environment
* Git
* GitHub

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/AgroMind.git
```

Navigate into the project:

```bash
cd AgroMind
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the required packages:

```bash
pip install pandas numpy scikit-learn fastapi uvicorn
```

---

# ▶️ Running the Application

Start the FastAPI backend from the project root:

```bash
uvicorn backend.main:app --reload
```

The backend will start at:

```text
http://127.0.0.1:8000
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates the Swagger UI, allowing API endpoints to be tested directly from the browser.

---

# 🔌 Backend Structure

The backend acts as the bridge between the user interface and the machine learning modules.

```text
Frontend
   │
   │ HTTP Request
   ▼
FastAPI
   │
   ├── AgroMind Engine
   │
   └── Soil Diagnosis
          │
          ▼
    Machine Learning
          │
          ▼
     Prediction
          │
          ▼
     JSON Response
```

The main backend entry point is:

```text
backend/main.py
```

The ML modules are organized inside:

```text
ml/
```

including:

```text
ml/agromind_engine.py
ml/soil_diagnosis.py
```

---

# 💡 Example Input

A user can provide agricultural parameters such as:

```text
Nitrogen       : 90
Phosphorus     : 42
Potassium      : 43
Temperature    : 25.5
Humidity       : 80
pH             : 6.5
Rainfall       : 200
```

The system processes the input through the machine learning pipeline and produces a crop recommendation.

---

# 📤 Example Output

```text
Recommended Crop: [Predicted Crop]
```

The exact prediction depends on the values supplied by the user.

---

# 🎯 Objectives

The main objectives of AgroMind are:

1. Provide data-driven crop recommendations.
2. Help farmers understand important soil parameters.
3. Reduce guesswork in crop selection.
4. Demonstrate the practical application of machine learning in agriculture.
5. Provide an API-based architecture that can be extended into a larger agricultural platform.
6. Make agricultural technology easier to use.

---

# 🌍 Real-World Impact

Agriculture often depends on several factors such as soil composition, weather conditions, rainfall, temperature, and humidity.

Choosing an unsuitable crop can result in:

* Lower productivity
* Wasted resources
* Financial losses
* Inefficient use of water and fertilizers

AgroMind attempts to address part of this problem by using historical agricultural data and machine learning to provide **data-driven crop recommendations**.

---

# 🔮 Future Enhancements

AgroMind can be expanded with several additional capabilities:

### 📷 Plant Disease Detection

Allow farmers to upload an image of a plant and use computer vision to identify possible diseases.

### 🌦️ Weather Integration

Integrate real-time weather information to improve recommendations.

### 🌐 Multilingual Support

Support regional languages so that farmers can interact with the application more easily.

### 📱 Mobile Application

Develop Android/iOS applications for easier field usage.

### 📴 Offline Prediction

Deploy lightweight models that can perform predictions without requiring continuous internet connectivity.

### 📈 Advanced Analytics

Provide information such as:

* Crop yield prediction
* Soil health trends
* Fertilizer recommendations
* Weather-based farming suggestions
* Historical crop performance

---

# 🔐 Limitations

The current version is primarily a machine-learning-based recommendation system and should be treated as a **decision-support tool**, not a replacement for professional agricultural advice.

Prediction quality depends on:

* Quality of input data
* Dataset coverage
* Accuracy of soil measurements
* Environmental conditions
* Machine learning model performance

---

# 🧪 Reproducibility

The project uses:

```text
random_state = 42
```

for the train-test split to make the machine learning experiment reproducible.

The preprocessing scaler is also persisted so that the same transformation can be used during prediction.

---

# 👨‍💻 Development Environment

The project was developed using:

```text
Operating System : Windows
IDE               : Visual Studio Code
Language          : Python
Backend           : FastAPI
ML                : Scikit-learn
API Server        : Uvicorn
Version Control   : Git / GitHub
```

---

# 📌 Learning Outcomes

Through AgroMind, the following concepts were implemented and practiced:

* Python programming
* Data preprocessing
* Exploratory data handling
* Outlier detection
* IQR methodology
* Feature scaling
* Machine learning
* Train-test splitting
* Model persistence
* REST API development
* FastAPI
* Uvicorn
* Frontend-backend integration
* Git and GitHub
* Machine learning application development

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

```bash
git clone <repository-url>
cd AgroMind
```

Create a new branch:

```bash
git checkout -b feature/new-feature
```

Make your changes and commit:

```bash
git add .
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/new-feature
```

Then create a Pull Request.

---

# 📜 License

This project is developed for **educational and demonstration purposes**.

---

# 👨‍💻 Author

**Sumanth Venigandla**

B.Tech — VIT-AP University

AgroMind — AI-powered smart agriculture and crop recommendation system.

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub!
