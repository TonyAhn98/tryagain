import os
import sys

GRID_SIZE = 20

icon_position = 0

grid = [["0" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

while True:
    os.system("clear")

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if col == icon_position:
                grid[row][col] = "1"
            else:
                grid[row][col] = "0"

    for row in grid:
        print(" ".join(row))

    print("\nPress Enter to move the icon to the right...", end="")
    sys.stdout.flush()
    input()
    icon_position += 1



