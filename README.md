#  Power Fault Monitoring System

## Overview

I built a Power Fault Monitoring System that detects power faults and sends alerts when an issue occurs. This system **is a demo** that simulates power data, trains an AI model to recognize faults, and integrates an alert system for real-time notifications. While the project showcases key concepts, it has several limitations and challenges that need to be addressed before real-world deployment.

##  Features

###  1. Power Fault Monitoring Dashboard (Streamlit)
Developed an interactive dashboard to track power faults visually. Simulates real-time monitoring by refreshing every few seconds. Displays key metrics like voltage, frequency, power generation, and fault status.

### 2. AI-Based Fault Detection
Trained a machine learning model using past power system data. AI learns from features like voltage, frequency, power generation, and past faults to predict potential issues. Identifies faults automatically based on input data.

### 3. Automated Alert System (Firebase + Twilio)
When a fault is detected, the system sends alerts via:
- **Firebase** (cloud database) for storing fault logs.
- **Twilio** (SMS notifications) to instantly notify relevant personnel.

#### Why Firebase and Twilio Files Are Not in the Repo
The Firebase and Twilio configuration files are not included in the repository because they contain sensitive credentials (API keys, auth tokens). These are stored in **environment variables** and referenced securely in the code using `.env` files, which are not pushed to GitHub to protect security and privacy.

##  Challenges Faced

### This is a Demo – Not a Fully Functional System
This project is a **proof-of-concept** and is not yet ready for real-world implementation due to the following challenges:

- **No Real-Time Data** – The system does not use actual sensor readings; it relies on simulated data created with Pandas.
- **Limited Training Data** – The AI model might not generalize well since it was trained on past, limited data.
- **Potential Overfitting** – The model performed too well on training data, meaning it may struggle with real-world faults.
- **Scalability Issues** – The system would need cloud deployment and efficient data pipelines for real-time processing.
- **Alert System Limitations** – Delays in notifications could be problematic in critical fault scenarios.

##  Why This Matters

 **Early Fault Detection** – Power companies can use AI to detect faults before they cause major blackouts.
**Real-Time Monitoring Potential** – If connected to live sensors, this system could provide instant updates on power faults.
 **Future Smart Grid Integration** – With improvements, this could become part of a fully automated power monitoring system.

##  Next Steps & Future Improvements

- Integrate **real-time sensor data** instead of simulated data.
- Improve model generalization with a **larger and more diverse dataset**.
- Deploy the system to the **cloud** for scalability.
- Optimize the **alert system** to reduce false positives and latency.

This project serves as an initial exploration of AI-based fault detection in power systems, demonstrating potential while highlighting areas for further development.





##  Live Demo  
Check out the live Power Fault Monitoring Dashboard:  
🔗 **[Power Fault Monitoring System](https://2khqsbsndcetvtwvhdhd4c.streamlit.app/)**

