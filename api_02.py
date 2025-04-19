import requests as rq

newpost = { 'title': 'My first API post!',
    'body': 'Hello world from Python!',
    'userId': 1

}

response = rq.post('https://jsonplaceholder.typicode.com/posts', json = newpost)

print (response.status_code)
print (response.json())
