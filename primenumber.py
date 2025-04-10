for i in range (2, 8):
    print (8/i)

for i in range (2, 8):
    if 8 % i == 0:
        print ('because of ', i, ' not prime')

print ('NEXT')

n = 19  # input
prime = True
for i in range (2, n):
    if n % i == 0:
        prime = False

if prime:
    print ('prime')
else:
    print ('not prime')

print ('NEXT')


def isprime(n):
    prime = True
    for i in range (2, int(n**.5) + 1):
        if n % i == 0:
            prime = False
    return prime

print(isprime(18))

print ('NEXT')

log_prime = 0
for i in range (1, 1500):
    if isprime (i) == True:
        log_prime = log_prime + 1
    
print ('there is ', log_prime, ' prime number in selected range')