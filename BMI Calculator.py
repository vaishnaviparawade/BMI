#BMI Calculator
weight = float(input("Enter Weight in Kg: "))
height = float(input("Enter Height in Meters: "))

height_in_meters = height / 100
BMI=weight / (height_in_meters**2)
print(BMI)


if(BMI >= 16 and BMI <=18.5):
    print ("You are Underweight"), BMI

elif(BMI >= 18.5 and BMI <24):
    print ("You are Healthy"), BMI

elif(BMI >= 25 and BMI <30):
    print ("You are Overweight"), BMI

elif(BMI >=30):
    print ("You are Obesed"), BMI   