import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Roller!")
    while True:
        sides = input("Enter the number of sides on the dice (or 'q' to quit): ")
        if sides.lower() == 'q':
            break
        if not sides.isdigit() or int(sides) < 1:
            print("Please enter a valid positive number.")
            continue
        sides = int(sides)
        result = roll_dice(sides)
        print(f"You rolled a {result} on a {sides}-sided dice.")
        again = input("Roll again? (y/n): ")
        if again.lower() != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

