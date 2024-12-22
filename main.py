import random 

# Define the possible choices for the game
rand = (0, 1, -1)

# Randomly select a choice for the computer from the defined options
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

# Convert the user's choice to its corresponding string representation
a = rev[my]

# Convert the computer's choice to its corresponding string representation
b = rev[computer]

# Print the choices made by the user and the computer
print(f"user choose= {a}\nComputer choose {b}")

# Determine the outcome of the game
if(my == computer):
    print("Draw!")  # If both choices are the same, it's a draw
else:
    # Check the conditions for user winning
    if(my == 0 and computer == 1):
        print("Snake drinks water, so user wins!")  # User wins
    elif(my == 0 and computer == -1):
        print("Gun shoots snake, so computer wins!")  # Computer wins
    elif(my == 1 and computer == 0):
        print("Snake drinks water, so computer wins!")  # Computer wins
    elif(my == 1 and computer == -1):
        print("Water can't shoot gun, so user wins!")  # User wins
    elif(my == -1 and computer == 0):
        print("Gun shoots snake, so user wins!")  # User wins
    elif(my == -1 and computer == 1):
        print("Water can't shoot gun, so computer wins!")  # Computer wins
    else:
        print("Something went wrong")  # Fallback for unexpected cases