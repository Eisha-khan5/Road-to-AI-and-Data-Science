height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
print(bmi)

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you have a normal weight")
elif bmi < 30:
    print("you are overweight")
elif bmi < 35:
    print("you are obese")
else:
    print("you are clinically obese")