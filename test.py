import requests

url : str = "http://127.0.0.1:5000/"

# app = requests.put(url + "open", json={"appname" : "git"})
command = requests.put(url + "command", json={"command" : "sleep"})

# print(app.json())
print(command.json())