
# 🌾 Data-Driven Crop Advisory System

This project aims to develop a smart crop advisory system using soil macronutrients and environmental parameters such as temperature, humidity, rainfall, and pH level. The system is designed to assist farmers—especially small and marginal ones—in making scientific decisions for crop selection and fertilizer usage.

---
## 📎 Project Presentation

📥 [Download PPT: Crop Advisory Project](Crop_Advisory_Project_with_KPIs.pptx)
---

# TEAM ID - 81
👨‍💻 Team Members
- Smruti Ranjan Nayak (24CSE322)
- Pritsh Behera (24ECE079)
- Suraj Panda (24CSE092)
- Aditya Sharma (24CSEAIML110)

---
## Demo video
## 🎯 Objective

To recommend the most suitable crop and fertilizer strategy based on:
- Soil Macronutrients (Nitrogen, Phosphorus, Potassium)
- Temperature
- Humidity
- pH
- Rainfall

---

## 📊 Dataset

**Source:** [Kaggle Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)  
**Size:** 2200 samples  
**Features:** N, P, K, temperature, humidity, pH, rainfall, label (crop name)

---

## 🛠️ Tools & Technologies

- Python (Jupyter Notebook)
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn (Random Forest Classifier, Logistic Regression)

---

## 📌 KPIs (Key Performance Indicators)

### 🌡️ Temperature_Category
- Cool Season: < 20°C  
- Warm Season: 20–30°C  
- Hot Season: > 30°C

### 🌧️ Rainfall_Level
- Low: < 100 mm  
- Medium: 100–200 mm  
- High: > 200 mm

### 🌱 Macronutrient Levels
**Nitrogen (N)**  
- Low: < 20 mg/kg  
- Medium: 20–90 mg/kg  
- High: > 90 mg/kg  

**Phosphorus (P)**  
- Low: < 20 mg/kg  
- Medium: 20–60 mg/kg  
- High: > 60 mg/kg  

**Potassium (K)**  
- Low: < 20 mg/kg  
- Medium: 20–45 mg/kg  
- High: > 45 mg/kg

---

## 🤖 Machine Learning

- **Primary Model:** Random Forest Classifier  
  → Achieved up to 98% accuracy
- **Baseline Model:** Logistic Regression

---

## 📈 Visualizations

- Histogram of temperature, rainfall, and NPK distributions
- Countplots for rainfall and temperature KPIs
- Barplot of top crops by temperature

---

## 🚀 Conclusion & Impact

This system empowers farmers with scientific decision-making, leading to:
- Better crop yield
- Lower fertilizer costs
- Improved soil health

---

## 🔭 Future Scope

- Integrate real-time sensor data
- Develop a mobile/web interface
- Add pest & disease prediction modules using satellite data
