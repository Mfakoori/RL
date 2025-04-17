
def guess_is_correct(digits):
    return True


for guesses in range(0, 100000):
    pin_temp = str (guesses).zfill(5)

    digits = {}
    digits ['1st'] = pin_temp [0]
    digits ['2nd'] = pin_temp [1]
    digits ['3rd'] = pin_temp [2]
    digits ['4th'] = pin_temp [3]
    digits ['5th'] = pin_temp [4]
    print (digits)
