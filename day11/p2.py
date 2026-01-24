import sys
from intcode import RunStatus, IntCodeComputer

DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computer = IntCodeComputer(program)

    white = {(0, 0)}

    direction = 0
    x, y = 0, 0

    while True:
        computer.fetch_input(1 if (x, y) in white else 0)
        status = computer.run(max_outputs=2, clear_outputs=True)
        if status == RunStatus.HALTED:
            break

        color, turn = computer.outputs
        if color == 1:
            white.add((x, y))
        else:
            white.discard((x, y))

        direction = (direction + (1 if turn == 1 else -1)) % 4
        dx, dy = DIR[direction]
        x, y = x + dx, y + dy

    min_x = min(x for x, y in white)
    max_x = max(x for x, y in white)
    min_y = min(y for x, y in white)
    max_y = max(y for x, y in white)

    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            row.append('#' if (x, y) in white else ' ')
        print(''.join(row))

if __name__ == '__main__':
    main()
