import sys, re
from itertools import combinations
from math import lcm

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    positions = []
    for line in data:
        positions.append([int(x) for x in re.findall(r'-?\d+', line)])

    def find_cycle(pos):
        vel = [0] * len(pos)
        initial_state = (tuple(pos), tuple(vel))
        steps = 0

        while True:
            for i, j in combinations(range(len(pos)), 2):
                if pos[i] < pos[j]:
                    vel[i] += 1
                    vel[j] -= 1
                elif pos[i] > pos[j]:
                    vel[i] -= 1
                    vel[j] += 1

            for i in range(len(pos)):
                pos[i] += vel[i]

            steps += 1

            if (tuple(pos), tuple(vel)) == initial_state:
                return steps

    initial_x, initial_y, initial_z = zip(*positions)

    cycle_x = find_cycle(list(initial_x))
    cycle_y = find_cycle(list(initial_y))
    cycle_z = find_cycle(list(initial_z))

    print(lcm(cycle_x, cycle_y, cycle_z))

if __name__ == '__main__':
    main()
