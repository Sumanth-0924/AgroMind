import pandas as pd

data = pd.read_csv("data/Crop_recommendation.csv")

print("First 5 rows:")
print(data.head())

print("\nShape:", data.shape)

print("\nMissing values:")
print(data.isnull().sum())