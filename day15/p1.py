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
    visited = {(0, 0)}

    while q:
        x, y, dist, computer = q.popleft()

        for i, (dx, dy) in enumerate(DIR):
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                continue

            computer_copy = deepcopy(computer)
            computer_copy.fetch_input(i + 1)
            computer_copy.run(clear_outputs=True)

            output = computer_copy.outputs[0]

            if output == 0:
                visited.add((nx, ny))
            elif output in (1, 2):
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1, computer_copy))

                if output == 2:
                    print(dist + 1)
                    return

if __name__ == '__main__':
    main()
