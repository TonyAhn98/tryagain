import os
import sys

# Define the size of the grid
GRID_SIZE = 20

# Define the position of the icon
icon_position = 0

# Create the grid
grid = [["0" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Loop until the user quits
while True:
    # Clear the screen
    os.system("clear")

    # Update the grid with the current position of the icon
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if col == icon_position:
                grid[row][col] = "1"
            else:
                grid[row][col] = "0"

    # Print the grid to the screen
    for row in grid:
        print(" ".join(row))

    # Wait for the user to press Enter
    print("\nPress Enter to move the icon to the right...", end="")
    sys.stdout.flush()
    input()
    icon_position += 1



