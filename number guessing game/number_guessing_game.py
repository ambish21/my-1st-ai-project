import random

print("🎯 Welcome to Number Guessing Game!")

while True:  # 🔁 Game repeat loop

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:  # 🎮 Guessing loop
        guess = int(input("Enter your guess (1-10): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts.")
            break   # guessing loop break

    # 👉 YAHAN add karna hai play_again
    play_again = input("Play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing! 👋")
        break   # outer loop break (game end)
