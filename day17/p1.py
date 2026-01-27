import sys
from intcode import RunStatus, IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    robot = IntCodeComputer(program)

    status = robot.run()
    assert status == RunStatus.HALTED
    view = list(map(chr, robot.outputs))

    grid = ''.join(view).strip().split('\n')
    H, W = len(grid), len(grid[0])

    alignment_sum = 0
    for r in range(1, H - 1):
        for c in range(1, W - 1):
            if grid[r][c] != '#':
                continue
            if all(grid[nr][nc] == '#' for nr, nc in
                   [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]):
                alignment_sum += r * c

    print(alignment_sum)

if __name__ == '__main__':
    main()
