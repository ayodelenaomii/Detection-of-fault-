import pandas as pd
import time
import random
import streamlit as st

# Set page config
st.set_page_config(page_title="⚡ Power Fault Monitoring Dashboard", layout="wide")
st.title("⚡ Power Fault Monitoring Dashboard")

# Function to generate simulated fault data
def generate_fault_data():
    return pd.DataFrame([[
        random.uniform(48.0, 52.0),   # highest_frequency
        random.uniform(48.0, 52.0),   # lowest_frequency
        random.uniform(210.0, 250.0), # highest_voltage
        random.uniform(200.0, 230.0), # lowest_voltage
        random.uniform(350.0, 500.0), # peak_generation
        random.uniform(100.0, 200.0), # lowest_generation
        random.uniform(10.0, 30.0),   # interrupted_power
        random.randint(0, 1),         # equipment_health
        random.randint(0, 1),         # weather_condition
        random.randint(0, 3),         # faults
        random.randint(1, 5),         # transmission_line
        random.uniform(10.0, 20.0),   # Voltage Range
        random.uniform(45.0, 55.0),   # Frequency Range
        random.uniform(80.0, 120.0),  # Power Generation Range
        random.uniform(0.01, 0.05)    # Normalized Power Interruptions
    ]], columns=[
        'highest_frequency', 'lowest_frequency', 'highest_voltage', 'lowest_voltage', 
        'peak_generation', 'lowest_generation', 'interrupted_power', 'equipment_health', 
        'weather_condition', 'faults', 'transmission_line', 'Voltage Range', 
        'Frequency Range', 'Power Generation Range', 'Normalized Power Interruptions'
    ])

# Initialize session state
if "fault_data" not in st.session_state:
    st.session_state.fault_data = generate_fault_data()

# Ensure there's at least one row in the dataframe
if st.session_state.fault_data.empty:
    st.session_state.fault_data = generate_fault_data()

# Display Key Metrics
col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

col1.metric("⚠️ Active Faults", int(st.session_state.fault_data["faults"].sum()))
col2.metric("🔌 Average Voltage", f"{st.session_state.fault_data['highest_voltage'].mean():.1f} V")
col3.metric("🌡️ Power Interruptions", f"{st.session_state.fault_data['interrupted_power'].mean():.1f} kW")
col4.metric("⚖️ Voltage Fluctuation", f"{(st.session_state.fault_data['highest_voltage'] - st.session_state.fault_data['lowest_voltage']).mean():.1f} V")
col5.metric("🎚️ Frequency Fluctuation", f"{(st.session_state.fault_data['highest_frequency'] - st.session_state.fault_data['lowest_frequency']).mean():.1f} Hz")
col6.metric("🔋 Minimum Power Generation", f"{st.session_state.fault_data['lowest_generation'].min():.1f} MW")
col7.metric("⚡ Peak Power Generation", f"{st.session_state.fault_data['peak_generation'].max():.1f} MW")
col8.metric("📊 Fault Rate", f"{(st.session_state.fault_data['faults'] / st.session_state.fault_data['transmission_line']).mean():.2f} per line")
col9.metric("🌤️ Weather Impact", f"{(st.session_state.fault_data['weather_condition'].mean() * 100):.1f}% Bad Weather")

# Live Fault Data Table
st.subheader("📊 Live Fault Data")
st.dataframe(st.session_state.fault_data)

# Refresh Button (Click to add new data)
if st.button("🔄 Refresh Data"):
    new_data = generate_fault_data()
    st.session_state.fault_data = pd.concat([st.session_state.fault_data, new_data], ignore_index=True)

# Display the last 10 data points
st.dataframe(st.session_state.fault_data.tail(10))

# Graph: Line Chart of Voltage and Power
st.subheader("📈 Fault Data Trends")
st.line_chart(st.session_state.fault_data[['highest_voltage', 'lowest_voltage', 'peak_generation']])

# Simulate Fault Alerts
alert_box = st.empty()

def generate_fault_alert():
    if random.choice([True, False]):
        alert_box.error("⚠️ New Fault Detected! Immediate Action Required.")
    else:
        alert_box.empty() 

# Auto-refresh for live updates
for _ in range(10):  # Simulates updates 10 times (adjust as needed)
    time.sleep(5)  # Simulated delay of 5 seconds
    new_data = generate_fault_data()  # Generate new simulated data
    st.session_state.fault_data = pd.concat([st.session_state.fault_data, new_data], ignore_index=True)  # Update table
    generate_fault_alert()  # Generate new fault alert
    st.rerun()  # Refresh Streamlit app
