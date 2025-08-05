import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import re

df = pd.read_csv("Cars Datasets 2025.csv",encoding='unicode_escape')
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
print(df.isnull().sum())
print(df.dropna(inplace=True))
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)
print(df.columns)
print(df.duplicated().sum())
print(df.median(numeric_only=True))

df['Seats'] = pd.to_numeric(df['Seats'], errors='coerce')

def clean_torque(value):
    if pd.isna(value):
        return np.nan
    nums = [int(n) for n in re.findall(r'\d+', str(value))]
    return sum(nums)/len(nums) if nums else np.nan

df['Torque'] = df['Torque'].apply(clean_torque)

df.dropna(subset=['Seats', 'Torque'], inplace=True)
print("\n🔍 Cleaned Data Types:\n", df.dtypes)
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
print("\n📊 Numeric Columns Found:\n", numeric_cols)

for col in numeric_cols:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # Histogram
    sns.histplot(df[col], bins=15, kde=True, ax=axes[0])
    axes[0].set_title(f"Histogram of {col}")
# Boxplot
    sns.boxplot(y=df[col], ax=axes[1])
    axes[1].set_title(f"Boxplot of {col}")
    
    plt.tight_layout()
    plt.show()

if len(numeric_cols) <= 5:
    sns.pairplot(df[numeric_cols])
    plt.suptitle("Pairplot of Numeric Features", y=1.00)
    plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()