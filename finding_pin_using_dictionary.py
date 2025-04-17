def guess_is_correct(digits):
    return (digits['3rd'] + digits ['5th'] == 14 and \
    digits['1st'] == 2*digits['2nd'] - 1 and \
    digits['4th'] == digits['2nd'] + 1 and \
    digits['2nd'] + digits['3rd'] == 10 and \
    digits['1st'] + digits['2nd'] + digits['3rd'] + digits['4th'] + digits['5th'] == 30)


for guesses in range(0, 100000):
    pin_temp = str (guesses).zfill(5)

    digits = {}
    digits ['1st'] = int(pin_temp [0])
    digits ['2nd'] = int(pin_temp [1])
    digits ['3rd'] = int(pin_temp [2])
    digits ['4th'] = int(pin_temp [3])
    digits ['5th'] = int(pin_temp [4])
    
    if guess_is_correct(digits):
        print (guesses)