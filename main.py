import random

def guess_number():
    # Initialize the range and counter for guessing
    low, high, tries = 1, 100, 0

    # Prompt the user to enter a number for the script to guess
    number = int(input("Enter a number between 1 and 100 for the script to guess: "))

    while True:
        # Generate a random guess within the current range
        guess = random.randint(low, high)
        print(f"My guess is {guess}.")
        tries += 1

        # Check if the guess is correct
        if guess == number:
            print(f"I guessed your number {guess} correctly in {tries} tries!")
            break
        # Adjust the range if the guess is too high.
        # 1 is just a basic number i noticed is pretty alright, you can also change it
        elif guess > number: # if the guess is higher than the number you typed in
            print("Too high!")
            high = guess - 1
        # Adjust the range if the guess is too low
        else: # if the guess is lower than the number you typed in. it is basically the same as:
                """elif guess < number:"""
              # but you can also just use else... well anyways, to not destroy the formation i will stop talking now
            print("Too low!")
            low = guess + 1

# Entry point for the script
if __name__ == "__main__":
    guess_number()