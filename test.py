import requests

url : str = "http://127.0.0.1:5000/open"

response = requests.put(url, {"app name" : "whatsapp"})

print(response.json())