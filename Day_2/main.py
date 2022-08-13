# Beginner

# print(type(10))
# print(type(10.99))
# print(type('M'))
# class Car():
#     pass
# bmw = Car()
# print(type(bmw))

# 35 => 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit)
# print(result)


# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# Body Mass Index => <18.5 Underweight, 18.5-25 Normal weight, 25-30 Overweight, >30 Obese
# result = (weight/(height*height))
# result = (weight/height ** 2)
# print(int(result))

# age = int(input("What is your current age:?"))
# days = (90 - age) * 365
# weeks = (90 - age) * 52
# months = (90 - age) * 12
# print(f"You have {days}, {weeks} weeks and {months} months left.")

# PROJECT
# Create a greeting for your program.
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How much people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(round(bill_per_person, 2))
print(f"Each person should pay: ${final_amount}")