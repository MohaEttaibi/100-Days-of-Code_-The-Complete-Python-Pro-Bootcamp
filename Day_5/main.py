# Beginner 

# students_heights = [180, 124, 165, 173, 189, 169, 146]
# 180 124 165 173 189 169 146
# 156 178 165 171 187
# students_heights = input("Input a list student heights ").split()
# for n in range(0, len(students_heights)):
#     students_heights[n] = int(students_heights[n])

# # Sum 
# total_height = 0
# for height in students_heights:
#     total_height += height
# print(total_height)

# # Len
# number_of_student = 0
# for student in students_heights:
#     number_of_student += 1
# print(number_of_student)

# print(round(sum(students_heights)/len(students_heights)))


# student_scores = [180, 124, 165, 173, 189, 169, 146]
# heighest_score = max(student_scores)
# lowest_score = min(student_scores)
# print(heighest_score)
# print(lowest_score)

# heighest_score = 0
# for score in student_scores:
#     if score > heighest_score:
#         heighest_score = score
# print(f"The heighest score in the class is: {heighest_score}")


# total = 0 
# for number in range(2, 101, 2):
#     total += number
# print(total)

# total2 = 0 
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)


# FizzBuzz Job Interview
# for number in range(1,101):
#     if(number % 3 == 0 and number % 5 == 0):
#         print("FizzBuzz")
#     elif(number % 5 == 0):
#         print("Buzz")
#     elif(number % 3 == 0):
#         print("Fizz")
#     else:
#         print(number)


# Password Generator
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
'V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+','-','=','@','^']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level -> fht^618
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# random.shuffle(password)
# print("Your password is: " + password)

# Hard Level -> g^9@h!h
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password = ""
for char in password_list:
    password += char
print("Your password is: " + password)