prime = True
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


print(isprime(18))