import requests

# The URL provided by Replit for your Flask server
url = 'http://127.0.0.1:5000'

# Send a GET request to the home endpoint
# response = requests.get(url)
# print(response.json())

# Send a GET request to the example endpoint
example_url = f'{url}/get/patients'
with requests.get(example_url, stream=True) as r:
  # Do things with the response here.
  response = requests.get(example_url)
  print(response.json())
