import requests as rq
url = "https://jsonplaceholder.typicode.com/posts/1"
response = rq.get(url)
data = response.json()
print (data)
