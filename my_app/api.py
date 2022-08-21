import requests

url ="https://arab04.pythonanywhere.com/api/menu/"
response =requests.get(url)
r =response.json()
for i in r:
	print(i['Name'])