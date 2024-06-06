import requests
import json

response = requests.get('https://www.ecfr.gov/api/admin/v1/agencies.json')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    # Pretty print the JSON data
    print(json.dumps(json_data, indent=4))
else:
    # If the request was unsuccessful, print an error message
    print(f'Error: {response.status_code}')