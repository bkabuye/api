import requests

BASE = "http://127.0.0.1:8000/"

payload = {"likes":10, "name": "Avengers", "views": 100000}
headers = {'accept': 'application/json'}

data = [{"likes":78, "name": "Avengers", "views": 100000}, 
        {"likes":43, "name": "Superman", "views": 230000}, 
        {"likes":10, "name": "python", "views": 1000},
        {"likes":100, "name": "Education", "views": 156000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/"+str(i), json=data[i])
    print(response.json())


reponse = requests.delete(BASE + "video/0")
print(reponse)

input()

response = requests.get(BASE + "video/2")
print(response.json())