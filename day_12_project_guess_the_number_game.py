import random

num = []
for i in range(1, 101):
    num.append(i)
gus = random.choice(num)

gg = input("Hard or easy?")

if gg == "easy":
    tr = 10  
elif gg == "hard":
    tr = 5  

print("The number is between 1 and 100")

# Game loop: Continue until user guesses correctly or runs out of attempts
while tr > 0:
    n = int(input("Guess the number: "))

    # Check if the guessed number is higher than the target number
    if n > gus:
        print("Too high")
        tr -= 1  
        print(f"Tries left: {tr}")

    # Check if the guessed number is lower than the target number
    elif n < gus:
        print("Too low")
        tr -= 1  
        print(f"Tries left: {tr}")

    # If the guess is correct, the player wins and the game ends
    elif n == gus:
        print("You win!")
        break

# If no attempts are left, the player loses and the correct number is revealed
if tr == 0:
    print(f"You lose! The correct number was {gus}")
