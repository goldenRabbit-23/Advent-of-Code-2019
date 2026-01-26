import sys
from intcode import IntCodeComputer
from collections import deque
from copy import deepcopy

DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    main_computer = IntCodeComputer(program)

    q = deque([(0, 0, 0, main_computer)])
    space = {(0, 0)}
    wall = set()
    oxygen_x, oxygen_y = 0, 0

    while q:
        x, y, dist, computer = q.popleft()

        for i, (dx, dy) in enumerate(DIR):
            nx, ny = x + dx, y + dy
            if (nx, ny) in space or (nx, ny) in wall:
                continue

            computer_copy = deepcopy(computer)
            computer_copy.fetch_input(i + 1)
            computer_copy.run(clear_outputs=True)

            output = computer_copy.outputs[0]

            if output == 0:
                wall.add((nx, ny))
            elif output in (1, 2):
                space.add((nx, ny))
                q.append((nx, ny, dist + 1, computer_copy))

                if output == 2:
                    oxygen_x, oxygen_y = nx, ny

    q = deque([(oxygen_x, oxygen_y, 0)])
    visited = {(oxygen_x, oxygen_y)}
    max_dist = 0

    while q:
        x, y, dist = q.popleft()
        max_dist = max(max_dist, dist)

        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if (nx, ny) in space and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1))

    print(max_dist)

if __name__ == '__main__':
    main()
