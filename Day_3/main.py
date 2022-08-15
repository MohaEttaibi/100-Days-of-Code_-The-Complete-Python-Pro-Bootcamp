# Beginner
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height > 20:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("The number is Even.")
# else:
#     print("The number is Odd.")

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# # Body Mass Index => <18.5 Underweight, 18.5-25 Normal weight, 25-30 Overweight, >30 Obese
# # result = (weight / (height * height))
# result = round((weight / height ** 2))
# if result < 18.5:
#     print("Under Weight")
# elif result < 25:
#     print("Normal Weight")
# elif result < 30:
#     print("Over Weight")
# elif result < 35:
#     print("Obese")
# else:
#     print("Clinically Obese")

# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap")
#         else:
#             print("Not leap")
#     else:
#         print("Leap")
# else:
#     print("Not leap")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is you age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == 'Y':
#         bill += 3

#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#   Pizza Order Practice
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is : ${bill}")

#   Love Calculator
# print("Welcome to the love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# name = name1 + name2
# lower_name = name.lower()
# t = lower_name.count('t')
# r = lower_name.count('r')
# u = lower_name.count('u')
# e = lower_name.count('e')
# true = t + r + u + e
# l = lower_name.count('l')
# o = lower_name.count('o')
# v = lower_name.count('v')
# e = lower_name.count('e')
# love = l + o + v + e
# love_score = int(str(true) + str(love))
# if (love_score < 10) or (love_score > 90):
#     print(f"Your score is {love_score} %, you go together like coke and mentos.") 
# elif (love_score >= 40) or (love_score <= 50):
#     print(f"Your score is {love_score} %, you are alright together.") 
# else:
#     print(f"Your score is {love_score} %.") 


# PROJECT
print('Welcome to Tresure Island.\nYour mission is to find the treasure.\nYou\'re at a crossroad.')
x = input('Where do you want to go? Type "left" or "right\n').lower()
if x == 'left':
    y = input('Type "swim" or "wait"\n').lower()
    if y == 'wait':
        z = input('Which door? "blue" or "red" or "yellow"\n').lower()
        if z == 'red':
            print("Game Over")
        elif z == 'yellow':
            print("You Win")
        elif z == 'blue':
            print("Game Over")
        else: 
            print("Game Over!")
    else:
        print("Game Over")
else:
    print("Game Over")