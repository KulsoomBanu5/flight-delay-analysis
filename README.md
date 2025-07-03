# flight-delay-analysis
Data-driven analysis of U.S. flight delays using Python and Random Forest
# ✈️ Flight Delay Analysis Using Python

A real-world data analysis project using a 1.9M-row flight delay dataset  
to explore patterns, identify causes of delays, and build an interpretable predictive model.

## 📊 Objectives
- Analyze delays by hour, weekday, month, airline, airport, and distance
- Identify top delay causes for most delayed airlines
- Map airport and airline codes to readable names
- Build a basic predictive model (Random Forest) for estimating delays

## 🔍 Key Insights
- Flights after 5 PM tend to have higher delays due to cascading effects.
- JetBlue Airways had the highest average delay, mostly due to late-arriving aircraft.
- December and July showed the highest delays (seasonal trends).
- Regional airports like CMX, ACY, and PLN had surprisingly high average delays.
- Delay prediction modeling attempted but was constrained by local compute limits.

## 🛠️ Tools Used
- Python (Pandas, Seaborn, Scikit-learn)
- Jupyter Notebook
- Random Forest Regressor
- Data Preprocessing & Visualization

## 🔗 Dataset
> [Download: DelayedFlights.csv](https://www.kaggle.com/datasets/usdot/flight-delays)

## 📌 Future Work
- Host model training on cloud (Google Colab / AWS)
- Improve predictive model with feature engineering
- Add airline-specific delay forecasts

---
