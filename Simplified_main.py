import random 

# Define the possible choices for the game
rand = (0, 1, -1)

# Randomly select a choice for the computer
computer = random.choice(rand)

# Display the options to the user
print("""choose the options below
      0-->Snake
      1-->Water
      -1-->Gun
      """)

# Get the user's choice as an integer
my = int(input("enter the choices mention above"))

# Create dictionaries to map choices to their respective values and vice versa
dic = {"snake": 0, "water": 1, "Gun": -1}
rev = {0: 'snake', 1: "water", -1: "gun"}

# Get the string representation of the user's and computer's choices
a = rev[my]
b = rev[computer]

# Print the choices made by the user and the computer
print(f"user choose= {a}\nComputer choose {b}")

# Check for a draw
if my == computer:
    print("Draw!")
else:
    # Determine the winner based on the difference between user and computer choices
    # The logic is simplified based on the outcomes of the game
    if ((my - computer) == -1) or ((my - computer) == 2):
        print('user wins')  # User wins in these cases
    else:
        print("computer wins!")  # Computer wins in all other cases