import requests
import json
from time import sleep

# Define the API endpoint
API_ENDPOINT = "http://127.0.0.1:8000/api/gps/"

# Define the JSON data with GPS points
DATA = [
    {"latitude": "35.70937", "longitude": "-0.65681", "timestamp": "2024-04-09T20:22:32Z"}, #start
    {"latitude": "35.70921", "longitude": "-0.65610", "timestamp": "2024-04-09T20:22:37Z"},
    {"latitude": "35.70905", "longitude": "-0.65569", "timestamp": "2024-04-09T20:22:42Z"},
    {"latitude": "35.70905", "longitude": "-0.65569", "timestamp": "2024-04-09T21:22:42Z"},# end same spot
    {"latitude": "35.70886", "longitude": "-0.65550", "timestamp": "2024-04-10T20:22:47Z"},# start
    {"latitude": "35.70807", "longitude": "-0.65474", "timestamp": "2024-04-10T20:22:52Z"},
    {"latitude": "35.70792", "longitude": "-0.65418", "timestamp": "2024-04-10T20:22:57Z"}, 
    {"latitude": "35.70787", "longitude": "-0.65380", "timestamp": "2024-04-11T21:23:02Z"},# close last
    {"latitude": "35.70789", "longitude": "-0.65380", "timestamp": "2024-04-11T21:23:02Z"}, 

]

# Send each GPS point as a POST request
for point in DATA:
    # Send the GPS point as a POST request to the API endpoint
    response = requests.post(API_ENDPOINT, json=point)
    # Check if the request was successful
    if response.status_code == 201:
        print("GPS point sent successfully:", point)
    else:
        print("Failed to send GPS point:", point)
    # Add a small delay (optional)
    sleep(1)  # Adjust the delay as needed
