import random

# step 1 assign some words in list and then choose a random word and assign it to the variable
words_list = ['bottle', 'envelope', 'knife']

# stages of hangman (ASCII art)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

choosen_word = random.choice(words_list)

# for testing
print("The chosen word is:", choosen_word)

# create a list called display and for each letter add "_" in display
display = []
a = len(choosen_word)

# create a variable called lives to keep track of number of lives (set to 6)
lives = 6

for b in range(a):
    display += "_"

print(display)

# a while loop to let the user guess again
# the loop should stop once the user guesses all the letters or loses all lives
end_of_game = False

# step 2 ask the user to guess a letter and make it lowercase
while not end_of_game:
    guess = input("Enter the letter of guess: ").lower()

    # step 3 check if the letter is present in the chosen word
    # loop through each position in the chosen word
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = guess

    # if guessed letter is not correct, reduce lives
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    # check if user has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You win")

    # print the ASCII stage according to current lives
    print(stages[lives])
