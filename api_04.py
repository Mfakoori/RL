import requests as rq
from datetime import datetime , time
url = 'https://api.sunrisesunset.io/json?lat=35.7219&lng=51.3347'
res = rq.get(url)
print(res.text, '\n \n \n')
r = res.json()['results']
print('sunrise in Tehran: ', r['sunrise'],'\nsunset in Tehran:  ' , r['sunset'], '\n \n \n \n')

sunset = r['sunset']
sunset = datetime.strptime( sunset, '%I:%M:%S %p') # Parsed into a datetime object
sunset = sunset.strftime ('%I:%M:%S %p') # reformatting

current_time = datetime.now()
current_time = current_time.strftime('%I:%M:%S %p')

import time
while current_time < sunset:
    time.sleep(60)
else:
    print ('sunset: ', sunset, 'current_time: ', current_time)

def mysms (number):
    my_api_key = '336F786D367A426543342F4A6B51706B3335764465775735733473594F72587A444F6E57635431304E70383D'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' % my_api_key #this % my_api_key used to be replased with %s inside the string
    mypayload = {'receptor':'09350540507', 'message': 'hi there, you have typed %i' % number} # this %i recieves integer value from outside of the string

