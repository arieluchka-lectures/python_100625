import requests
import json

print("=" * 60)
print("PYTHON REQUESTS MODULE - BASIC CAPABILITIES")
print("=" * 60)

# 1. BASIC GET REQUEST
print("\n1. Simple GET Request:")
print("-" * 40)
response = requests.get('https://httpbin.org/get')
print(f"Status Code: {response.status_code}")
print(f"Response OK: {response.ok}")
print(f"URL: {response.url}")

# 2. GET REQUEST WITH PARAMETERS
print("\n2. GET Request with Query Parameters:")
print("-" * 40)
params = {
    'name': 'Python',
    'version': '3.11',
    'library': 'requests'
}
response = requests.get('https://httpbin.org/get', params=params)
print(f"URL with params: {response.url}")
print(f"Response JSON: {json.dumps(response.json()['args'], indent=2)}")

# 3. POST REQUEST
print("\n3. POST Request with Data:")
print("-" * 40)
data = {
    'username': 'pythonuser',
    'message': 'Hello from requests!'
}
response = requests.post('https://httpbin.org/post', data=data)
print(f"Status Code: {response.status_code}")
print(f"Form data sent: {response.json()['form']}")

# 4. POST REQUEST WITH JSON
print("\n4. POST Request with JSON:")
print("-" * 40)
json_data = {
    'title': 'Learn Requests',
    'completed': False
}
response = requests.post('https://httpbin.org/post', json=json_data)
print(f"JSON sent: {response.json()['json']}")

# 5. CUSTOM HEADERS
print("\n5. Request with Custom Headers:")
print("-" * 40)
headers = {
    'User-Agent': 'Python Requests Tutorial',
    'Accept': 'application/json',
    'Custom-Header': 'MyValue'
}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(f"Headers received by server:")
print(json.dumps(response.json()['headers'], indent=2))

# 6. RESPONSE PROPERTIES
print("\n6. Response Object Properties:")
print("-" * 40)
response = requests.get('https://httpbin.org/get')
print(f"Status Code: {response.status_code}")
print(f"Headers: {dict(list(response.headers.items())[:3])}...")  # Show first 3 headers
print(f"Content Type: {response.headers['Content-Type']}")
print(f"Encoding: {response.encoding}")
print(f"Response Time: {response.elapsed.total_seconds()} seconds")

# 7. DIFFERENT HTTP METHODS
print("\n7. Different HTTP Methods:")
print("-" * 40)
methods = {
    'GET': requests.get('https://httpbin.org/get'),
    'POST': requests.post('https://httpbin.org/post', data={'key': 'value'}),
    'PUT': requests.put('https://httpbin.org/put', data={'key': 'value'}),
    'DELETE': requests.delete('https://httpbin.org/delete'),
    'PATCH': requests.patch('https://httpbin.org/patch', data={'key': 'value'})
}
for method, resp in methods.items():
    print(f"{method}: Status {resp.status_code}")

# 8. TIMEOUT AND ERROR HANDLING
print("\n8. Timeout and Error Handling:")
print("-" * 40)
try:
    # Set a timeout of 5 seconds
    response = requests.get('https://httpbin.org/delay/2', timeout=5)
    print(f"Request completed in {response.elapsed.total_seconds():.2f} seconds")
except requests.exceptions.Timeout:
    print("Request timed out!")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# 9. SESSION OBJECT (maintains cookies and settings)
print("\n9. Using Session Objects:")
print("-" * 40)
session = requests.Session()
session.headers.update({'User-Agent': 'Session Example'})
# All requests made with this session will use these headers
response1 = session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
response2 = session.get('https://httpbin.org/cookies')
print(f"Cookies maintained in session: {response2.json()['cookies']}")

# 10. STATUS CODE CHECKING
print("\n10. HTTP Status Code Handling:")
print("-" * 40)
response = requests.get('https://httpbin.org/status/200')
if response.status_code == 200:
    print("✓ Success (200 OK)")
elif response.status_code == 404:
    print("✗ Not Found (404)")
else:
    print(f"Status: {response.status_code}")

print("\n" + "=" * 60)
print("End of Requests Module Capabilities Demo")
print("=" * 60)
