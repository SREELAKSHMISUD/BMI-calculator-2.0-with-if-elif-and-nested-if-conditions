# if, else, elif ,nested if conditions with BMI calculator for weight calculation example

height = float(input("Enter your height in m: "))

weight = int(input("Enter your weight in kg: "))

BMI=weight/height**2
if(BMI <= 18.5):
  print("Your BMI is "+ str(BMI) + ", you are underweight." )
elif(BMI<25):
  print("Your BMI is "+ str(BMI) + ", you have a normal weight.")

elif(BMI <30):
  print("Your BMI is "+ str(BMI)+ ", you are slightly overweight.")
elif(BMI<35):
  print("Your BMI is "+ str(BMI)+ ", you are obese.")
else:
  print("Your BMI is "+ str(BMI) + ", you are clinically obese.")
