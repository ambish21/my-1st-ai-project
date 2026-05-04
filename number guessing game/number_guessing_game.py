import random

print("🎯 Welcome to Number Guessing Game!")

# Random number generate (1 to 10)
secret_number = random.randint(1, 10)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed in {attempts} attempts.")
        break
