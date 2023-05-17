import random
import time
import sys
import os

# Define the dimensions of the grid
GRID_SIZE = 20

# Define the number of animals to start with
NUM_ZEBRAS = 100
NUM_LIONS = 5

# Define the number of steps before an animal can breed or die
ZEBRA_BREEDING_TIME = 5
LION_BREEDING_TIME = 8
LION_DEATH_TIME = 3

# Define the symbols for each animal type
ZEBRA_SYMBOL = 'Z'
LION_SYMBOL = 'L'
EMPTY_SYMBOL = '.'

class Animal:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.age = 0
    
    def __repr__(self):
        return self.symbol
    
    def move(self):
        # Move the animal to a random neighboring cell
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        new_x = (self.x + dx) % GRID_SIZE
        new_y = (self.y + dy) % GRID_SIZE
        self.x, self.y = new_x, new_y
        self.age += 1
    
    def breed(self):
        # Create a clone of the animal at a random neighboring cell
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        new_x = (self.x + dx) % GRID_SIZE
        new_y = (self.y + dy) % GRID_SIZE
        return type(self)(new_x, new_y)
    
class Zebra(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, ZEBRA_SYMBOL)
    
    def update(self, animals):
        self.move()
        if self.age >= ZEBRA_BREEDING_TIME:
            animals.append(self.breed())
            self.age = 0

class Lion(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, LION_SYMBOL)
        self.hunger = 0
    
    def update(self, animals):
        self.move()
        self.hunger += 1
        nearby_zebras = [a for a in animals if isinstance(a, Zebra) and abs(a.x - self.x) <= 1 and abs(a.y - self.y) <= 1]
        if nearby_zebras:
            self.hunger = 0
            target = random.choice(nearby_zebras)
            animals.remove(target)
        if self.hunger >= LION_DEATH_TIME:
            animals.remove(self)
        elif self.age >= LION_BREEDING_TIME:
            animals.append(self.breed())
            self.age = 0

# Initialize the grid with empty cells
grid = [[EMPTY_SYMBOL for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Add the initial animals to the grid
animals = []
for i in range(NUM_ZEBRAS):
    x, y = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)
    animals.append(Zebra(x, y))
for i in range(NUM_LIONS):
    x, y = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)
    animals.append(Lion(x, y))

# Run the simulation
step = 0
# Initialize the time stamp
timestamp = 0

# Main simulation loop
while True:
    # Print the current grid
    print(f"Time: {timestamp}")
    for row in grid:
        print(' '.join(row))
    
    # Wait for user input to proceed to the next step
    if input("Press Enter to continue or q to quit :").lower() == 'q':
        sys.exit()
    
    # Update the animals
    for animal in animals:
        animal.update(animals)
    
    # Update the grid with the new animal locations
    grid = [[EMPTY_SYMBOL for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for animal in animals:
        grid[animal.y][animal.x] = animal.symbol
    
    # Increment the time stamp
    timestamp += 1