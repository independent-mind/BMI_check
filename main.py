height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height ** 2)

result = int(round(BMI, 0))

if result < 18.5:
  print(f"Your BMI is {result}, you are underweight.")
elif result < 25:
  print(f"Your BMI is {result}, you have a normal weight.")
elif result < 30:
  print(f"Your BMI is {result}, you are slightly overweight.")
elif result < 35:
  print(f"Your BMI is {result}, you are obese.")
else:
  print(f"Your BMI is {result}, you are clinically obese.")
  
