import requests
 
url = 'http://localhost:5000/'

response = requests.post(url)

print(response.text)