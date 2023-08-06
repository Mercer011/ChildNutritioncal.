def bmiCal(Weight, Height):
    bmi = (Weight / (Height ** 2)) * 703
    return bmi

def details():
    print("Nutrition Calculator:")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    Gender = input("M/F: ")
    Height = float(input("Enter your height (in inches): "))
    Weight = float(input("Enter your Weight (in pounds): "))

    bmi = bmiCal(Weight, Height)

    if age >= 0 and age < 2:
        mini_cal = 800
    elif age >= 2 and age < 4:
        mini_cal = 1400
    elif age >= 4 and age < 8:
        mini_cal = 1800
    else:
        mini_cal = 0

    print("\nChild Information")
    print("Name:", name)
    print("Age:", age, "years old")
    print("Gender:", Gender)
    print("Height:", Height)
    print("Weight:", Weight)
    print("BMI:", bmi)

    if bmi < 16:
        print("Severely UnderWeight")
    elif 16 <= bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Healthy")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obese")

    daily_intake_in_cal = 0
    food = ["milk", "egg", "rice", "lentils", "vegetables", "Meat"]
    calval = [100, 150, 130, 113, 185, 143]

    print("\nDaily Food Consumption")
    for i in range(len(food)):
        quantity = float(input(f"{food[i]} (in grams): "))
        daily_intake_in_cal += (quantity / 100) * calval[i]

    print("\nDaily calorie Consumption:", daily_intake_in_cal, "Calories")

   

details()
