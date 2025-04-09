def bmi (weight, height):
    bmi = weight/ (height*height)
    if bmi < 18.5:
        print("you're underweighted and your BMI is ", bmi)
    elif bmi >= 18.5 and bmi <= 24.9:
        print ("you're in shape and youre BMI is ", bmi)
    else:
        print ("you're definitely overweighted, your BMI is ", bmi)



bmi (62, 1.71)
