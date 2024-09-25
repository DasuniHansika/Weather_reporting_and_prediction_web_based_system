# Weather Reporting and Prediction System

## Overview
This project is a **Weather Reporting and Prediction System** that gathers real-time data using an ESP32 module and DHT11 sensor, processes it through a Python Flask web application, and predicts future weather conditions using a machine learning model trained on a CSV dataset.

## Features
- **Real-time Data Collection:** Collects temperature and humidity data using the DHT11 sensor connected to the ESP32 module.
- **Web Interface:** Displays real-time weather data through a Flask web application.
- **Weather Prediction:** Utilizes a Random Forest model to predict future weather conditions based on historical data.
- **Data Storage:** Weather data is stored in a CSV file and can be accessed for analysis.

## Technology Stack
- **Hardware:** ESP32 Module, DHT11 Sensor
- **Backend:** Python Flask
- **Machine Learning:** Random Forest Model
- **Database:** CSV (for training and data storage)

## System Workflow
1. **Data Collection:** The ESP32 module collects real-time temperature and humidity data using the DHT11 sensor.
2. **Data Storage:** Collected data is stored in a CSV file and sent to the Flask web app.
3. **Machine Learning:** The stored data is used to train a Random Forest model to predict future weather conditions.
4. **Web Application:** Flask serves the real-time data and predictions via a user-friendly interface.

## Installation Guide
### Requirements:
- ESP32 Module
- DHT11 Sensor
- Python 3.x
- Flask
- scikit-learn
- pandas

### Steps:
1. **Set up Hardware:**
   - Connect the DHT11 sensor to the ESP32 module.
   - Ensure proper wiring and connectivity.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/weather-reporting-system.git
   cd weather-reporting-system

Install Dependencies:
pip install -r requirements.txt

Run Flask Application:
python app.py

Train the Model:
Ensure your CSV dataset is properly formatted.

Run the script to train the Random Forest model:
python train_model.py

Access the Web App:
Open your browser and navigate to http://localhost:5000 to view real-time weather data and predictions.

Contributors
Nisal Basura Wickramasinghe
Dasuni Hansika
