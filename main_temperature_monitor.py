import time
import random
import csv
from datetime import datetime

# Configurable thresholds
MIN_TEMP = 18.0  # Minimum temperature threshold (Celsius)
MAX_TEMP = 28.0  # Maximum temperature threshold (Celsius)
DATA_FILE = 'temperature_log.csv'
POLL_INTERVAL = 2  # Seconds between readings

def read_temperature():
    """Mock function to simulate reading temperature from a sensor."""
    # Replace this logic with actual sensor reading code (e.g., using Adafruit_DHT or w1thermsensor for DS18B20)
    return round(random.uniform(15.0, 32.0), 2)

def log_temperature(timestamp, temp):
    """Append temperature reading to a CSV file."""
    with open(DATA_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, temp])

def alert(temp):
    """Print an alert if the temperature is out of range."""
    if temp < MIN_TEMP:
        print(f"ALERT: Temperature too low! Measured: {temp}°C (Min: {MIN_TEMP}°C)")
    elif temp > MAX_TEMP:
        print(f"ALERT: Temperature too high! Measured: {temp}°C (Max: {MAX_TEMP}°C)")

def display_reading(timestamp, temp):
    print(f"{timestamp}: {temp}°C")

def main():
    # Write CSV header if file does not exist
    try:
        with open(DATA_FILE, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Temperature (C)'])
    except FileExistsError:
        pass

    print("Starting temperature monitoring...")
    try:
        while True:
            temp = read_temperature()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            display_reading(timestamp, temp)
            log_temperature(timestamp, temp)
            alert(temp)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("\nTemperature monitoring stopped.")

if __name__ == "__main__":
    main()