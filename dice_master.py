import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Roller App 🎲")

while True:
    user_input = input("Roll the dice? (y/n): ").lower()
    
    if user_input == 'y':
        result = roll_dice()
        print(f"🎲 You rolled a {result}!")
    elif user_input == 'n':
        print("Thanks for playing! Goodbye 👋")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
