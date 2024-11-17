import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext
import configparser  # Import configparser to read the configuration file

# Function to fetch glucose data from the API
def get_glucose_data(patient_id, token):
    url = f"https://api.libreview.io/llu/connections/{patient_id}/graph"  # Corrected URL with dynamic patient_id
    
    headers = {
        'Authorization': f'Bearer {token}',  # Use the actual token
        'Content-Type': 'application/json',
        'product': 'llu.ios',
        'version': '4.7.0'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to extract glucose values
def get_glucose_value(data):
    if data:
        try:
            glucose_measurement = data['data']['connection']['glucoseMeasurement']
            glucose_value = glucose_measurement['Value']
            timestamp = glucose_measurement['Timestamp']
            trend_arrow = glucose_measurement['TrendArrow']
            return glucose_value, timestamp, trend_arrow
        except KeyError as e:
            print(f"KeyError: {e} - Check the API response structure.")
            return None, None, None
    return None, None, None

# Function to load configuration from file
def load_config():
    config = configparser.ConfigParser()
    config.read('config.conf')  # Read the configuration file

    # Retrieve patient_id and token from the config file
    patient_id = config['API']['patient_id']
    token = config['API']['token']
    
    return patient_id, token

# Main function for managing data retrieval and GUI updates
class GlucoseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Glucose Tracker")
        self.root.geometry("400x400")  # Set a fixed size for the window
        self.root.resizable(False, False)  # Make the window non-resizable
        self.root.configure(bg="#2E2E2E")  # Dark gray background

        self.glucose_readings = []  # Store last readings
        self.patient_id, self.token = load_config()  # Load patient ID and token from config

        # Create a ScrolledText widget for better formatting
        self.text_widget = scrolledtext.ScrolledText(root, width=50, height=20, bg="#1C1C1C", fg="white", wrap=tk.WORD)
        self.text_widget.pack(pady=5)

        self.update_button = tk.Button(root, text="Refresh Data", command=self.update_data, bg="#444", fg="white")
        self.update_button.pack(pady=5, anchor='e')

        self.root.after(0, self.update_data)  # Start data retrieval

    def update_data(self):
        data = get_glucose_data(self.patient_id, self.token)
        glucose_value, timestamp, trend_arrow = get_glucose_value(data)

        if glucose_value is not None:
            self.glucose_readings.append((glucose_value, timestamp, trend_arrow))
            if len(self.glucose_readings) > 20:
                self.glucose_readings.pop(0)  # Keep only the last readings

            self.display_glucose_readings()
        else:
            messagebox.showwarning("Warning", "Failed to retrieve glucose data.")

        # Repeat this function every 2 minutes
        self.root.after(120000, self.update_data)

    def display_glucose_readings(self):
        self.text_widget.delete(1.0, tk.END)  # Clear the current text widget

        # Display the readings in reverse order to show the most recent at the top
        for value, timestamp, trend_arrow in reversed(self.glucose_readings):
            color = self.get_color(value)
            trend_text = self.get_trend_text(trend_arrow)
            display_text = (
                f"Glucose Level: "
            )
            # Insert the glucose value with color formatting
            self.text_widget.insert(tk.END, display_text)
            self.text_widget.insert(tk.END, f"{value:.1f} mg/dL\n", "colored")  # Color only the glucose value
            self.text_widget.insert(tk.END, f"Trend: {trend_text}\n")
            self.text_widget.insert(tk.END, f"Timestamp: {timestamp}\n")
            self.text_widget.insert(tk.END, "-----------------------------------------------\n")

            # Tag the glucose value for coloring
            self.text_widget.tag_config("colored", foreground=color)

    def get_color(self, value):
        if 3.9 <= value <= 8.7:  # Normal range
            return "green"
        elif 3.4 <= value < 3.9 or 8.7 < value <= 9.2:  # Slightly out of range
            return "orange"
        else:  # Out of range
            return "red"

    def get_trend_text(self, trend_arrow):
        trend_map = {
            1: "Dropping Fast",
            2: "Going Low",
            3: "Stable",
            4: "Going High",
            5: "Increasing Fast"
        }
        return trend_map.get(trend_arrow, "Unknown")

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GlucoseTrackerApp(root)
    root.mainloop()
