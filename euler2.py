def IsEven(n):
    if n % 2 ==0:
        return True
    else:
        return False

sum = 0
first_num = 1
second_num = 2
while first_num <4*10**6 :
    if IsEven(first_num):
        sum = sum + first_num
    new_num = first_num + second_num
    first_num = second_num
    second_num = new_num
print (sum)