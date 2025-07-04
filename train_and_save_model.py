import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset (adjust filename if needed)
df = pd.read_csv("DelayedFlights.csv")

# Feature Engineering
df['DepHour'] = df['CRSDepTime'] // 100
df['TotalDelay'] = df['DepDelay'] + df['ArrDelay']

# Select relevant columns
model_df = df[['DepHour', 'DayOfWeek', 'Month', 'Distance', 'DepDelay', 'CRSElapsedTime',
               'UniqueCarrier', 'Origin', 'Dest', 'TotalDelay']].dropna()

# Downsample
model_df = model_df.sample(30000, random_state=42)

# One-hot encoding
model_df = pd.get_dummies(model_df, columns=['UniqueCarrier', 'Origin', 'Dest'], drop_first=True)

# Train-test split
X = model_df.drop('TotalDelay', axis=1)
y = model_df['TotalDelay']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=30, max_depth=15, random_state=42)
model.fit(X_train, y_train)

# Save model in Python 3.12-compatible format
joblib.dump(model, 'flight_delay_rf_model.pkl')

# Save column names for later input matching
joblib.dump(X.columns.tolist(), 'model_features.pkl')

print("✅ Model saved as 'flight_delay_rf_model.pkl'")
