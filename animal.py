import random

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            grid[self.y][self.x] = Empty(self.x, self.y)
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            grid[self.y][self.x].hp = 0
            grid[self.y][self.x] = self
            return True
        else:
            return False
        
    def move(self, direction='right'):
        print(f'moving to {direction}. <<<NOT IMPLEMENT YET>>>')
        self.x += 1

    def breed(self, x, y, grid):
        child = self.__class__(x, y)
        child.move_to(grid, target='.')
        grid[y][x] = self

    def get_neighbors(self, grid, target):
        world_height = len(grid)
        world_width = len(grid[0])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([x - 1, y])  # Left
        neighbors.append([x + 1, y])  # Right
        neighbors.append([x, y - 1])  # Up
        neighbors.append([x, y + 1])  # Down

        neighbors_valid = [neighbor for neighbor in neighbors
                           if neighbor[0] >= 0
                           and neighbor[0] < world_height
                           and neighbor[1] >= 0
                           and neighbor[1] < world_width
                           and str(grid[neighbor[0]][neighbor[1]]) == target]
        return neighbors_valid
class Empty(Animal):
    def __str__(self):
        return '.'

class Zebra(Animal):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 3
        self.age = 5

    def __str__(self):
        return 'Z'
    
    def move(self, grid):
        self.move_to(grid, target='.')

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 3 == 0

class Lion(Animal):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 10
        self.age = 10

    def __str__(self):
        return 'L'
    
    def move(self, grid):
        hunt_is_successful = self.move_to(grid, target='Z')
        if hunt_is_successful:
            self.hp = 3
            # grid[self.y][self.x] = 'L'
        else:
            self.move_to(grid, target='.')
            self.hp -= 1
        neighbors = self.get_neighbors(grid, target='Z')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            self.hp = 3
            return
        
        neighbors = self.get_neighbors(grid, target='.')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 8 == 0


class Grid:
    def __init__(self):
        self.grid = [['0' for _ in range(20)] for _ in range(20)]
        self.grid[0] = ['0' for _ in range(20)]
        self.grid[-1] = ['0' for _ in range(20)]
        for row in self.grid:
            row[0] = '0'
            row[-1] = '0'

    def display(self):
        for row in self.grid:
            print(' '.join(row))