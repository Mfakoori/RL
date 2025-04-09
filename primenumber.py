for i in range (2, 8):
    print (8/i)

for i in range (2, 8):
    if 8 % i == 0:
        print ('because of ', i, ' not prime')


n = 19  # input
prime = True
for i in range (2, n):
    if n % i == 0:
        prime = False

if prime:
    print ('prime')
else:
    print ('not prime')


def isprime(n):
    prime = True
    for i in range (2, n):
        if n % i == 0:
            prime = False
    return prime

if prime:
    print ('prime')
else:
    print ('not prime')


isprime(42)