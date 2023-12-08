# BMI Calculator

# variables:
weight = input("What is your current weight? In KG please.  \n Write here: ")
height = input("What is your current height? Please write like this - metres, centimetres (E.g.: 1.75) \n Write here: ")

f_weight = float(weight)
f_height = float(height)

BMI = round((f_weight / f_height) / f_height, 1)

weight_status = ""

if BMI <= 18.5:
  weight_status = "you might be underweight."
elif BMI > 18.5 and BMI <= 25:
  weight_status = "you have a normal weight."
elif BMI >= 25 and BMI <= 30:
  weight_status = "you might be overweight."
elif BMI >= 30 and BMI <= 35:
  weight_status = "you might have obesity, you should consult this with your doctor."
elif BMI > 40:
  weight_status = "you're heavily obese, seek professional help immediately."

print(f"Your BMI is {BMI}, {weight_status}")
