import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "Crop_recommendation.csv")

data = pd.read_csv(file_path)

# -----------------------------
# 1. Statistical summary
# -----------------------------
print("\nStatistical Summary:")
print(data.describe())

# -----------------------------
# 2. Crop distribution
# -----------------------------
plt.figure(figsize=(12,6))
sns.countplot(x='label', data=data)
plt.xticks(rotation=90)
plt.title("Crop Distribution")
plt.show()

# -----------------------------
# 3. Correlation heatmap
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# -----------------------------
# 4. Feature distributions
# -----------------------------
data.hist(figsize=(12,10))
plt.suptitle("Feature Distributions")
plt.show()