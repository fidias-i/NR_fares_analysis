import os
import subprocess
import json

# auth_url = "https://opendata.nationalrail.co.uk/authenticate"
# auth_out = os.system(f'curl {auth_url} --data-urlencode username={user}  --data-urlencode  password={password}')

# URL, username, and password
auth_url = "https://opendata.nationalrail.co.uk/authenticate"
json_file_path = 'credentials.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)  # Parse the JSON file into a dictionary

user = data["user"]
password = data["password"]

# Correctly define the curl command and arguments
command = [
    "curl", 
    "-X", "POST",               # Specify POST method
    "-H", "Content-Type: application/json",  # Specify headers
    "-d", f'{{"username":"{user}", "password":"{password}"}}',  # Data payload
    auth_url                     # Target URL
]

# Run the curl command and capture the output
result = subprocess.run(command, capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Parse the response (if it's JSON)
    response = result.stdout.strip()
    try:
        auth_data = json.loads(response)
        print(auth_data)  # Print the parsed dictionary
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
else:
    print("Command failed with error:", result.stderr)

auth_data.keys()
token  = auth_data['token']

auth_data['roles'].keys()



# Define the variables
version = '2.0'
item = 'fares'
# item = 'routeing'
# version = '3.0'
# item = 'timetable'

url = f"https://opendata.nationalrail.co.uk/api/staticfeeds/{version}/{item}"
auth_token = auth_data['token']
output_file = f"{item}.zip"

# Define the curl command
command = [
    "curl", 
    url,  # Target URL
    "-H", f"X-Auth-Token: {auth_token}",  # Header with the authentication token
    "--output", output_file  # Output file
]

# Run the curl command
result = subprocess.run(command, capture_output=True, text=True)

# Check for success
if result.returncode == 0:
    print(f"File downloaded successfully: {output_file}")
else:
    print("Command failed with error:")
    print(result.stderr)
