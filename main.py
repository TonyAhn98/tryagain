#import sys
#import os
from argparse import ArgumentParser
from circle_of_life import CircleOfLife

if __name__ == '__main__':
    #any_input = input('enter any input:')
    #print('hello AIE world!')
    parser = ArgumentParser()
    parser.add_argument('--timesteps', type=int, default=10)
    parser.add_argument('--world_size', type=int, default=20)
    parser.add_argument('--num_zebras', type=int, default=10)
    parser.add_argument('--num_lions', type=int, default=10)
    #parser.add_argument('--gretting', type=str, default='hi')
    #parser.add_argument('--name', type=str, default='unknown', help='your name')
    args = parser.parse_args()
    print(args)
    input('press enter to start')

    safari = CircleOfLife(args.world_size, args.num_zebras, args.num_lions)
    safari.run(args.timesteps)

    num_zebras, num_lions = safari.count_animals()
    print(f"Number of zebras: {num_zebras}")
    print(f"Number of lions: {num_lions}")
    #print('len', len(sys.argv))
    #for i, var in enumerate(sys.argv):
        #print(i, var)


    