import random

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0

    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            return True
        else:
            return False
        
    def move(self, direction='right'):
        print(f'moving to {direction}. <<<NOT IMPLEMENT YET>>>')
        self.x += 1

    def breed(self, x, y):
        print(f'breed to {x}, {y}. <<< NOT IMPLEMENTED >>>')
        # return Animal(x, y)

    def get_neighbors(self, grid, target):
        ''' target can be ., L, or Z
            returns a list of coordinates '''
        world_height = len(grid)
        world_width = len(grid[0])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([x - 1, y])
        neighbors.append([x + 1, y])
        neighbors.append([x, y - 1])
        neighbors.append([x, y + 1])
        neighbors_valid = [neighbor for neighbor in neighbors
                           if grid[neighbor[1]][neighbor[0]] == target
                           and neighbor[0] >= 0
                           and neighbor[0] < world_width
                           and neighbor[1] >= 0
                           and neighbor[1] < world_height]
        return neighbors


class Zebra(Animal):
    def move(self, grid):
        self.move_to(grid, target='.')

    def breed(self, x, y):
        print('<<< NOT IMPLEMENTED >>>')

class Lion(Animal):
    def move(self, grid):
        hunt_is_successful = self.move_to(grid, target='Z')
        if hunt_is_successful:
            self.hp = 3
        else:
            self.move_to(grid, target='.')
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


class grid:
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