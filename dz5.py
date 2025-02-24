import requests
import inspect

response = requests.get('https://fake-json-api.mock.beeceptor.com/users')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error - ", response.status_code)

print(inspect.ismodule(requests.get))
print(inspect.isclass(requests.Request))
print(inspect.isfunction(requests.get))