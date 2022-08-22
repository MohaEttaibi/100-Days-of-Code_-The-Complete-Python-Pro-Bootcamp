# Beginner 

# import math

# def area_calc(height, width, cover):
#     area = height * width
#     cans = math.ceil(area / cover)
#     print(f"You'll need {cans} cans of paint")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# area_calc(height=test_h, width=test_w, cover=coverage)


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime == False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)


# Caesar Cipher = PROJECT

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is : {end_text}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to continue, Otherwise type 'no'\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is : {cipher_text}")

# encrypt(plain_text=text,shift_amount=shift)

# def dencrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is : {cipher_text}")

# dencrypt(plain_text=text,shift_amount=shift)

# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction == "decode":
#     dencrypt(plain_text=text,shift_amount=shift)
