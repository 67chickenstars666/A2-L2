a =10
b =18
c = 6
if a and b and c:
    print("all numbers are boolean value as true")
else:
    print("at least one number is boolean value as false") 
a = 666
b = 89
c = 44
if a>0 or b>0 or c>0:
          print("either of the numbers are greater than zero")
else:
           print("none of the numbers are greater than zero")

 #bmi calculator
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
if bmi <=18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You have a normal weight.")
elif  bmi <= 29.9:
    print("You are overweight.")
elif bmi >=34.9:
      print("You are severely overweight.")
elif bmi <=39.9:
    print("You are morbidly obese.")
else:
    print("You are clinically obese.")
   

