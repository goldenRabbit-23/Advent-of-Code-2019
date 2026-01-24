import sys
from intcode import RunStatus, IntCodeComputer

DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computer = IntCodeComputer(program)

    white = set()
    painted = set()

    direction = 0
    x, y = 0, 0

    while True:
        computer.fetch_input(1 if (x, y) in white else 0)
        status = computer.run(max_outputs=2, clear_outputs=True)
        if status == RunStatus.HALTED:
            break

        color, turn = computer.outputs
        painted.add((x, y))
        if color == 1:
            white.add((x, y))
        else:
            white.discard((x, y))

        direction = (direction + (1 if turn == 1 else -1)) % 4
        dx, dy = DIR[direction]
        x, y = x + dx, y + dy

    print(len(painted))

if __name__ == '__main__':
    main()
