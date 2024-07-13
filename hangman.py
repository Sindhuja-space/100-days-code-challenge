import random
from decorators import stages, logo
from words import word_list

print(logo)

end_of_the_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []

for _ in range(word_length):
    display.append("_")

while not end_of_the_game:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_the_game = True
        print("You Win!")

    print(stages[lives])