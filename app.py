import streamlit as st
import pandas as pd
import joblib

# Load the trained model and input feature columns
model = joblib.load('flight_delay_rf_model.pkl')
feature_columns = joblib.load('model_features.pkl')  # X.columns from training

st.title("✈️ Flight Delay Predictor")
st.markdown("Estimate total delay based on flight info and current status.")


# User inputs
dep_hour = st.slider("Departure Hour (0–23)", 0, 23, 12)
day_of_week = st.selectbox("Day of the Week", [1, 2, 3, 4, 5, 6, 7])
month = st.selectbox("Month", list(range(1, 13)))
distance = st.number_input("Flight Distance (in miles)", value=500)
dep_delay = st.number_input("Departure Delay So Far (minutes)", value=0)
crs_elapsed = st.number_input("Scheduled Flight Duration (minutes)", value=120)

carrier = st.text_input("Airline Code (e.g., B6, DL, UA)", "B6")
origin = st.text_input("Origin Airport Code (e.g., JFK)", "JFK")
dest = st.text_input("Destination Airport Code (e.g., LAX)", "LAX")

if st.button("Predict Delay"):
    # Create input DataFrame
    input_df = pd.DataFrame(columns=feature_columns)
    input_df.loc[0] = 0  # Fill with zeros
    input_df.at[0, 'DepHour'] = dep_hour
    input_df.at[0, 'DayOfWeek'] = day_of_week
    input_df.at[0, 'Month'] = month
    input_df.at[0, 'Distance'] = distance
    input_df.at[0, 'DepDelay'] = dep_delay
    input_df.at[0, 'CRSElapsedTime'] = crs_elapsed

    # Set one-hot columns if they exist
    if f'UniqueCarrier_{carrier}' in input_df.columns:
        input_df.at[0, f'UniqueCarrier_{carrier}'] = 1
    if f'Origin_{origin}' in input_df.columns:
        input_df.at[0, f'Origin_{origin}'] = 1
    if f'Dest_{dest}' in input_df.columns:
        input_df.at[0, f'Dest_{dest}'] = 1

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"✈️ Predicted Total Delay: {round(prediction, 2)} minutes")
