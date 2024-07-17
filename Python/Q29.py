# Program to calculate bmi

h = float(input("Enter height in m: "))
w = float(input("Enter weight in kg: "))
bmi = w/(h**2)

if bmi<=18.5:
    print("Underweight")
elif 18.5<bmi<=24.9:
    print("Normal")
elif 24.9<bmi<=29.29:
    print("Overweight")
else:
    print("Obese")
