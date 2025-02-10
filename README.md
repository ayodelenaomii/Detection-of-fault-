⚡ Power Fault Monitoring System
📌 Overview
I built a Power Fault Monitoring System that detects power faults and sends alerts when an issue occurs. This system simulates power data, trains an AI model to recognize faults, and integrates an alert system for real-time notifications.

🖥️ Features
🚀 1. Power Fault Monitoring Dashboard (Streamlit)
Developed an interactive dashboard to track power faults visually.
Simulates real-time monitoring by refreshing every few seconds.
Displays key metrics like voltage, frequency, power generation, and fault status.
🤖 2. AI-Based Fault Detection
Trained a machine learning model using past power system data.
AI learns from features like voltage, frequency, power generation, and past faults to predict potential issues.
Identifies faults automatically based on input data.
📡 3. Automated Alert System (Firebase + Twilio)
When a fault is detected, the system sends alerts via:
Firebase (cloud database) for storing fault logs.
Twilio (SMS notifications) to instantly notify relevant personnel.
⚠️ Challenges Faced
❌ No Real-Time Data – The system does not use actual sensor readings; it relies on simulated data created with Pandas.
❌ Limited Training Data – The AI model might not generalize well since it was trained on past, limited data.
❌ Potential Overfitting – The model performed too well on training data, meaning it may struggle with real-world faults.

 Why This Matters
✅ Early Fault Detection – Power companies can use AI to detect faults before they cause major blackouts.
✅ Real-Time Monitoring Potential – If connected to live sensors, this system could provide instant updates on power faults.
✅ Future Smart Grid Integration – With improvements, this could become part of a fully automated power monitoring system.

🚀 Next Steps & Future Improvements
Integrate real-time sensor data instead of simulated data.
Improve model generalization with a larger and more diverse dataset.
Deploy the system to the cloud for scalability.
