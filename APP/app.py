import tkinter as tk
from tkinter import messagebox
import joblib
import mysql.connector
import numpy as np

# Load the saved model and label encoder
model = joblib.load('weather_prediction_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Function to fetch the latest temperature and humidity from the database
def get_latest_data():
    try:
        # Database connection parameters
        db_config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'iot_data'
        }

        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to fetch the latest temperature and humidity
        cursor.execute("SELECT temperature, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
        latest_data = cursor.fetchone()

        # Close the connection
        cursor.close()
        conn.close()

        return latest_data

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to update the display with the latest data
def update_display():
    latest_data = get_latest_data()
    if latest_data:
        temp_c, rel_hum = latest_data
        label_temp.config(text=f"{temp_c} °C")
        label_hum.config(text=f"{rel_hum} %")
    else:
        label_temp.config(text="N/A")
        label_hum.config(text="N/A")

# Function to predict the weather
def predict_weather():
    latest_data = get_latest_data()

    if latest_data:
        temp_c, rel_hum = latest_data
        
        # Prepare the input data
        input_data = np.array([[temp_c, rel_hum]])
        
        # Predict the weather
        prediction_encoded = model.predict(input_data)
        prediction = label_encoder.inverse_transform(prediction_encoded)
        
        # Display the prediction
        messagebox.showinfo("Prediction", f"The predicted weather is: {prediction[0]}")
    else:
        messagebox.showerror("Data Error", "Could not retrieve the latest data.")

# Initialize the main window
root = tk.Tk()
root.title("Weather Prediction App")

# Labels for displaying the latest temperature and humidity
tk.Label(root, text="Latest Temperature (C):").grid(row=0, column=0, padx=10, pady=10)
label_temp = tk.Label(root, text="N/A")
label_temp.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Latest Humidity (%):").grid(row=1, column=0, padx=10, pady=10)
label_hum = tk.Label(root, text="N/A")
label_hum.grid(row=1, column=1, padx=10, pady=10)

# Button to update the display with the latest data
update_button = tk.Button(root, text="Update Data", command=update_display)
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Button to predict the weather using the latest data from the database
predict_button = tk.Button(root, text="Predict Weather", command=predict_weather)
predict_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
