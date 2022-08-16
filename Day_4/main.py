# Beginner 

# import random

# side = random.randint(0, 1)

# if side == 1:
#     print("Head")
# else:
#     print("Tails")


# states = ['A','B','C']
# print(states)
# states.extend(['D'])
# print(states)
# 

# import random

# names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
# names_string = input("Give me everybody's names, seperated by a comma.\n")
# names = 'Angela,Ben,Jenny,Michael,Chloe'
# names = names_string.split(',')
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(random_choice)
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to buy the meal today.")


# row1 = ["😅", "😅", "😅"]
# row2 = ["😅", "😅", "😅"]
# row3 = ["😅", "😅", "😅"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?\n")
# horizontal = int(position[0])
# vertical = int(position[1])
# # selected_row = map[vertical -1 ]
# # selected_row[horizontal - 1] = "X"
# map[vertical -1][horizontal - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

import random

rock = "👊🏼"
paper = "🖐🏼"
scissors ="✌🏼"
# ur_choice = ["👊🏼","🖐🏼","✌🏼"]
game_imogi = [rock, paper, scissors]

ur_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if ur_choice >= 3 or ur_choice < 0:
    print("Invalid number entered, You lose")
else:
    print("You chose " + game_imogi[ur_choice])
    pc_choice = random.randint(0, 2)
    # print("You chose " + ur_choice[choice])
    # print(f"You chose {ur_choice}")
    # print(f"Computer chose {pc_choice}")
    print("Computer chose " + game_imogi[pc_choice]) 

    if ur_choice == 0 & pc_choice == 2:
        print("You win")
    elif pc_choice == 0 & ur_choice == 2:
        print("You lose")
    elif pc_choice > ur_choice:
        print("You lose")
    elif ur_choice > pc_choice:
        print("You win")
    elif pc_choice == ur_choice:
        print("It's a draw")

