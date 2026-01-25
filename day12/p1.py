import sys, re
from itertools import combinations

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    positions = []
    for line in data:
        positions.append([int(x) for x in re.findall(r'-?\d+', line)])
    velocities = [[0, 0, 0] for _ in positions]

    for _ in range(1000):
        # Apply gravity
        for (i, p1), (j, p2) in combinations(enumerate(positions), 2):
            for axis in range(3):
                if p1[axis] < p2[axis]:
                    velocities[i][axis] += 1
                    velocities[j][axis] -= 1
                elif p1[axis] > p2[axis]:
                    velocities[i][axis] -= 1
                    velocities[j][axis] += 1

        # Apply velocity
        for i in range(len(positions)):
            for axis in range(3):
                positions[i][axis] += velocities[i][axis]

    total_energy = 0
    for pos, vel in zip(positions, velocities):
        pot = sum(abs(x) for x in pos)
        kin = sum(abs(x) for x in vel)
        total_energy += pot * kin

    print(total_energy)

if __name__ == '__main__':
    main()
