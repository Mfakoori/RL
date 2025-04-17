a = {}
print (type (a))

tel = {'me': '001', 'friend 1': '002', 'friend 2': '003'}
print (tel)
tel['friend 3'] =  '004'
print (tel)
tel['friend 4'] = '005'
print (tel)
tel.pop('friend 3')
print (tel)
print('friend 1' in tel)
for b in tel:
    print (b)
for b in tel.items():
    print (b)
for k, v in tel.items():
    print ('key is ', k, 'value is', v)