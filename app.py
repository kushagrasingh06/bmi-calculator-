height=float(input("Height (cm): "))/100
weight=float(input("Weight (kg): "))

bmi=weight/(height*height)

print("BMI =",round(bmi,2))

if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")
