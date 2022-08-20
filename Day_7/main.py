# Beginner 

# Hangman
import random
from hangman_word import word_list

stages = ['''
    +---+
    |   |    
    0   |
   /|\  |
   / \  |
        |
  =======
''','''
    +---+
    |   |    
    0   |
   /|\  |
   /    |
        |
  =======
''','''
    +---+
    |   |    
    0   |
   /|\  |
        |
        |
  =======
''','''
    +---+
    |   |    
    0   |
   /|   |
        |
        |
  =======
''','''
    +---+
    |   |    
    0   |
        |
        |
        |
  =======
''','''
    +---+
    |   |    
        |
        |
        |
        |
  =======
''']

end_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"
# print(display)

while not end_game:
    geuss = input("Geuss a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessd letter: {geuss}")
        if letter == geuss:
            display[position] = letter
    # print(display)

    if geuss not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose!")
        

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win.")
    print(stages[lives])