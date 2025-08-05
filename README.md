# 🚗 Car Dataset - Exploratory Data Analysis (EDA)

This project performs **Exploratory Data Analysis (EDA)** on a car dataset using Python. It includes data cleaning, visualization, and insights from numeric features such as `Seats` and `Torque`.

---

## 📂 Dataset Overview

The dataset contains details like:
- **Company Name**
- **Car Model**
- **Engine**
- **Fuel Type**
- **Seats**
- **Torque**

---

## 📈 Visualizations

### 🔹 Histograms & Boxplots

<img src="screenshots/histogram_seats.png" width="45%"> <img src="screenshots/boxplot_seats.png" width="45%">
<img src="screenshots/histogram_torque.png" width="45%"> <img src="screenshots/boxplot_torque.png" width="45%">

### 🔹 Pairplot

<img src="screenshots/pairplot.png" width="80%">

### 🔹 Correlation Matrix

<img src="screenshots/correlation_matrix.png" width="80%">

---

## 🧼 Cleaning Performed

- Converted `Seats` and `Torque` to numeric values
- Handled values like `100 - 140 Nm` by averaging
- Removed rows with missing or invalid entries

---

## 🧠 Key Insights

- Majority of cars have **2 or 5 seats**.
- **High-torque outliers** detected (800–1000 Nm), likely performance/luxury cars.
- Weak or no correlation between `Seats` and `Torque`.

---


