# 🍬 Factory Reallocation & Shipping Optimization Recommendation System

> An AI-powered Decision Intelligence System for optimizing factory allocation, reducing shipping lead times, and improving supply chain efficiency for Nassau Candy Distributor.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)
![License](https://img.shields.io/badge/License-Academic-green.svg)

---

## 📌 Project Overview

The **Factory Reallocation & Shipping Optimization Recommendation System** is an end-to-end Machine Learning and Business Intelligence solution developed for **Nassau Candy Distributor**.

The project addresses the challenge of inefficient factory allocation by predicting shipping lead times, simulating alternative factory assignments, and recommending the most suitable production location based on operational efficiency, logistics cost, and business profitability.

Unlike traditional descriptive analytics, this project enables **data-driven decision-making** through predictive modeling, scenario simulation, and interactive visual analytics.

---

## 🎯 Business Problem

Nassau Candy Distributor currently relies on static factory assignment rules, leading to:

- High shipping lead times
- Increased logistics costs
- Inefficient factory utilization
- Margin erosion
- Limited visibility into alternative factory assignments

This project introduces a recommendation system capable of evaluating multiple allocation scenarios before implementation.

---

## 🚀 Project Objectives

- Predict shipping lead times using Machine Learning
- Simulate factory-product reassignment scenarios
- Recommend optimal factory allocations
- Reduce logistics costs
- Improve shipping efficiency
- Support strategic supply chain decisions
- Provide an interactive decision-support dashboard

---

# 📊 Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Lead Time Prediction
        │
        ▼
Route & Product Clustering
        │
        ▼
Factory Reallocation Simulation
        │
        ▼
Recommendation Engine
        │
        ▼
Business KPI Analysis
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 🧠 Machine Learning Models

The project compares multiple regression models for lead time prediction.

| Model | Purpose |
|---------|----------|
| Linear Regression | Baseline Model |
| Random Forest Regressor | Non-linear Prediction |
| Gradient Boosting Regressor | Final Selected Model |

### Model Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# 📈 Key Features

- Data Cleaning & Preprocessing
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Shipping Lead Time Prediction
- Factory Reallocation Recommendation Engine
- Route Performance Analysis
- Shipping Cost Estimation
- What-If Scenario Simulation
- KPI Dashboard
- Business Risk Assessment
- Interactive Streamlit Dashboard

---

# 🖥 Streamlit Dashboard Modules

- 📊 Executive Dashboard
- 🏭 Factory Optimization Simulator
- 🔄 What-If Scenario Analysis
- ⭐ Recommendation Dashboard
- ⚠ Risk & Impact Panel
- 📈 Factory Performance Summary
- 📋 KPI Summary
- 📥 Recommendation Report Download

---

# 📂 Project Structure

```
NASSAUPROJECTFOLDER/

│

├── datasets/
│   ├── orders.csv
│   ├── processed_orders.csv
│   ├── processed_orders_scaled.csv
│   ├── factory_master.csv
│   ├── product_factory_mapping.csv
│   ├── region_master.csv
│   ├── factory_recommendations.csv
│   └── kpi_summary.csv
│
├── DataPrepandFtEng.ipynb
├── ExploratoryDataAnalysis.ipynb
├── Lead_Time_Prediction.ipynb
├── Route&ProductClustering.ipynb
├── FactoryReallocation.ipynb
├── RecommendationAnalysis.ipynb
│
├── best_lead_time_model.pkl
├── app.py
├── style.css
├── requirements.txt
└── README.md
```

---

# 💻 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib
- Seaborn
- Joblib
- Streamlit

### Development Tools

- Jupyter Notebook
- VS Code
- GitHub

---

# 📊 Business KPIs

- Lead Time Reduction
- Shipping Cost Optimization
- Profit Impact Analysis
- Factory Workload Distribution
- Recommendation Coverage
- Scenario Confidence Score

---

# 📈 Expected Business Impact

The recommendation system helps decision-makers to:

- Reduce delivery lead time
- Improve factory utilization
- Lower logistics costs
- Increase operational efficiency
- Support intelligent factory allocation
- Enable data-driven supply chain optimization

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Factory-Reallocation-Shipping-Optimization-System.git
```

Move into the project folder

```bash
cd Factory-Reallocation-Shipping-Optimization-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📸 Dashboard Preview

> Add screenshots of your Streamlit dashboard here after deployment.

Example:

- Executive Dashboard
- Factory Optimization Simulator
- Recommendation Dashboard
- Risk Analysis Panel

---

# 📚 Future Enhancements

- Real-time shipment tracking
- Demand forecasting integration
- Route optimization algorithms
- Geographic route visualization
- Cloud database integration
- Multi-objective optimization
- Deep Learning-based prediction models

---

# 👨‍💻 Author

**Rihu Mishra**

AI & Machine Learning Student

---

# 📄 License

This project was developed for **academic learning and portfolio purposes**. The dataset and business scenario are used as part of an educational supply chain optimization project.
