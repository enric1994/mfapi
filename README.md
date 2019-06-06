# Multifile API with Flask and Docker

This repository pretends to be a boilerplate to process multiple files (such as images) in an isolate Docker container that provides an API to:
* Send multiple files + parameters
* Receive one processed file + parameters

I believe that it can be useful to integrate different parts of a pipeline that use different environments.

# Example

In the following example, two images are sent from the client to the server API alongside some parameters. Then, the API blends the images and return the result and some parameters:

```
import requests

# Load multiple files
files=dict(img1=open('img1.png'),img2=open('img2.png'))

# Create some parameters
payload = {'param1': '0.5', 'param2': ['value2.1', 'value2.2']}

# Send files and parameters
response = requests.post('http://localhost:5000/',
    params=payload,
    files=files)

# Save the received file
with open('response_file.png', 'wb') as f:
    f.write(response.content)

# Print the received parameters
print(response.headers.get('key1'))
print(response.headers.get('key2'))
```

# Usage

1- Use `docker-compose up` in the docker folder to start the Docker API.

2- The client send `img1.png`, `img2.png` and some parameters to the server. Use `python send_files.py`, in a new terminal.

3- The client will save the received file and print the returned parameters.
