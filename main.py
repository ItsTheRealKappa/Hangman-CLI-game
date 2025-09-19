import random


from hangman_words import word_list
from hangman_art import stages, logo

lives = 6



chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
previous_guesses = []
while not game_over:


    
    print("****************************<" + str(lives) + ">/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

   

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess in previous_guesses:
        print("You've already guessed " + guess)
    else:
        previous_guesses += guess
    print("Word to guess: " + display)

    

    if guess not in chosen_word:
        lives -= 1
        print(guess + " is not in the word. You lose a life")

        if lives == 0:
            game_over = True

            
            print("IT WAS "  + chosen_word + "!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    if lives == 6:
        print('''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''')

    elif lives == 5:
        print('''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''')

    elif lives == 4:
        print('''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''')

    elif lives == 3:
        print('''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''')

    elif lives == 2:
        print(r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''')

    elif lives == 1:
        print(r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''')

    elif lives == 0:
        print(r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''')

    if lives == 0:
        print("You lose.")
