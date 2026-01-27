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

    # Find starting position and direction
    for r in range(H):
        for c in range(W):
            if grid[r][c] in '^v<>':
                sr, sc = r, c
                direction = grid[r][c]

    # Follow the path
    path = []
    r, c = sr, sc
    dr, dc = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[direction]
    while True:
        # Try to move forward
        if 0 <= r + dr < H and 0 <= c + dc < W and grid[r + dr][c + dc] == '#':
            r += dr
            c += dc
            if path and isinstance(path[-1], int):
                path[-1] += 1
            else:
                path.append(1)
            continue

        # Try to turn right
        rdr, rdc = dc, -dr
        if 0 <= r + rdr < H and 0 <= c + rdc < W and grid[r + rdr][c + rdc] == '#':
            dr, dc = rdr, rdc
            path.append('R')
            continue

        # Try to turn left
        ldr, ldc = -dc, dr
        if 0 <= r + ldr < H and 0 <= c + ldc < W and grid[r + ldr][c + ldc] == '#':
            dr, dc = ldr, ldc
            path.append('L')
            continue

        break

    functions = {'A': None, 'B': None, 'C': None}
    main_routine = []
    def compress(i):
        # Routine complete
        if i == len(path):
            return True

        # Try to match existing functions
        for fname, fseq in functions.items():
            if fseq is not None and path[i:i+len(fseq)] == fseq:
                main_routine.append(fname)
                if compress(i + len(fseq)):
                    return True
                main_routine.pop()

        # Try to define a new function
        for fname in functions:
            if functions[fname] is None:
                for length in range(2, 11, 2):
                    candidate = path[i:i+length]
                    functions[fname] = candidate
                    main_routine.append(fname)
                    if compress(i + length):
                        return True
                    main_routine.pop()
                    functions[fname] = None
                break

        return False

    # Find valid compression
    compress(0)

    # Prepare input for the robot
    input_lines = [
        ','.join(main_routine),
        ','.join(map(str, functions['A'])),
        ','.join(map(str, functions['B'])),
        ','.join(map(str, functions['C'])),
        'n'
    ]
    input_str = '\n'.join(input_lines) + '\n'
    input_bytes = list(map(ord, input_str))

    robot.reset()
    robot.memory[0] = 2
    robot.fetch_input(*input_bytes)

    status = robot.run()
    assert status == RunStatus.HALTED
    print(robot.outputs[-1])

if __name__ == '__main__':
    main()
