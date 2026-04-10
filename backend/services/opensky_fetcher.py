# orbitviewer/backend/services/opensky_fetcher.py

import requests
import json
import time

# Placeholder for the OpenSky Network API URL
# Bounding box for the Washington D.C. area (latitude/longitude)
# lamax, lamin, lomax, lomin
BBOX_DMV = "39.27,-77.93,38.52,-76.15"
# All states endpoint is easier for initial testing
OPENSKY_API_URL = "https://opensky-network.org/api/states/all"

def fetch_flight_data():
    """
    Fetches real-time flight data from the OpenSky Network API.
    """
    print("Fetching flight data from OpenSky Network...")
    try:
        # The API does not require authentication for public data
        response = requests.get(OPENSKY_API_URL)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        data = response.json()
        print(f"Successfully fetched data for {len(data.get('states', []))} aircraft.")
        return data
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    
    return None

def save_data_to_file(data, filename="flight_data.json"):
    """
    Saves the fetched flight data to a JSON file.
    """
    if data:
        print(f"Saving data to {filename}...")
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Data saved successfully.")
        except IOError as io_err:
            print(f"Error saving data to file: {io_err}")

if __name__ == "__main__":
    flight_data = fetch_flight_data()
    if flight_data:
        # In a real application, this would be pushed to a database or message queue.
        # For now, we save it to a local file in the backend directory.
        save_data_to_file(flight_data, filename="backend/flight_data_sample.json")
