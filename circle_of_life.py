import random
from animal import Zebra, Lion, Empty
from utils import print_TODO

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.grid = [[Empty(y, x) for y in range(self.world_size)]
                                  for x in range(self.world_size)]
        random.seed(0)
        zebra_coords, lion_coords = self.get_random_coords(num_zebras, num_lions)
        self.zebras = []
        self.lions = []
        for y, x in zebra_coords:
            zebra = Zebra(x, y)
            self.grid[y][x] = zebra
            self.zebras.append(zebra)
        for y, x in lion_coords:
            lion = Lion(x, y)
            self.grid[y][x] = lion
            self.lions.append(lion)
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {num_zebras}')
        print(f'\tnumber of lions = {num_lions}')

    def get_random_coords(self, num_zebras, num_lions):
        all_coords = [(y, x) for y in range(self.world_size)
                      for x in range(self.world_size)]
        zebra_coords = random.sample(all_coords, num_zebras)
        all_coords = list(set(all_coords) - set(zebra_coords))
        lion_coords = random.sample(all_coords, num_lions)
        return zebra_coords, lion_coords

    def reset_grid(self):
        self.grid = [['.' for _ in range(self.world_size)]
                     for _ in range(self.world_size)]

    def initialize_grid(self):
        self.grid = [[' ' for _ in range(self.world_size)]
                     for _ in range(self.world_size)]

    def display(self):
        print(f'Clock: {self.timestep}')
        top_coord_str = ''.join([f'{coord+1:3}' for coord in range(len(self.grid))])
        print('  ' + top_coord_str)
        for row, line in enumerate(self.grid):
            buffer = [str(animal) for animal in line]
            print(f'{row:3} ' + '  '.join(buffer))
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)]
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)

    def step_breed(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)
                   and animal.is_ready_to_breed()]
        for animal in animals:
            animal.breed(animal.x, animal.y, self.grid)

    def clear_bodies(self):
        for y, line in enumerate(self.grid):
            for x, animal in enumerate(line):
                if isinstance(animal, Lion) or isinstance(animal, Zebra):
                    if animal.hp == 0:
                        self.grid[y][x] = Empty(y, x)

    def housekeeping(self):
        for y, line in enumerate(self.grid):
            for x, animal in enumerate(line):
                if isinstance(animal, Lion) or isinstance(animal, Zebra):
                    if animal.hp == 0:
                        self.grid[y][x] = Empty(y, x)
                    else:
                        self.grid[y][x].age += 1

    def count_animals(self):
        num_zebras = sum(isinstance(animal, Zebra) for line in self.grid for animal in line)
        num_lions = sum(isinstance(animal, Lion) for line in self.grid for animal in line)
        return num_zebras, num_lions

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            #import pdb
            #pdb.set_trace()
            self.step_move()
            self.display()  
            self.step_breed()
            self.display()
            self.clear_bodies()
            self.housekeeping()

#if __name__ == '__main__':
    #zebra = Zebra(0, 0)
    #lion = Lion(0, 0)
    #print(zebra.__class__)
    #print(Zebra)
    #print(lion.__class__)
    #print(Lion)
    #another_zebra = zebra.__class__(1, 1)
    #another_lion = lion.__class__(1, 1)
    #print(another_lion)
    #print(another_zebra)
    #safari = CircleOfLife(20,40,20)
    #safari.display()
    #safari.step_move()
    #safari.step_breed()
    #safari.run(100)
    #exit()