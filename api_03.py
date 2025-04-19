#sunrise and sunset in Tehran
import requests as rq
url = 'https://api.sunrisesunset.io/json?lat=35.7219&lng=51.3347'
res = rq.get(url)
print(res.text, '\n \n \n')
r = res.json()['results']
print('sunrise in Tehran: ', r['sunrise'],'\nsunset in Tehran:  ' , r['sunset'])

print ((r['sunset'][0:2]))