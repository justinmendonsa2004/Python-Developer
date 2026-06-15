import requests

a = requests.get("https://jsonplaceholder.typicode.com/users")
print(a.text)