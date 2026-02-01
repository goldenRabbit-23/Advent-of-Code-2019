import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    grid = [list(line) for line in data]
    H, W = len(grid), len(grid[0])
    seen = set()

    while True:
        h = ''.join(''.join(row) for row in grid)
        if h in seen:
            break
        seen.add(h)

        new_grid = [row[:] for row in grid]
        for r in range(H):
            for c in range(W):
                bugs = sum(
                    grid[nr][nc] == '#'
                    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                    if 0 <= nr < H and 0 <= nc < W
                )

                if grid[r][c] == '#' and bugs != 1:
                    new_grid[r][c] = '.'
                elif grid[r][c] == '.' and bugs in (1, 2):
                    new_grid[r][c] = '#'

        grid = new_grid

    print(sum(
        (1 << i) for i in range(H * W)
        if grid[i // W][i % W] == '#'
    ))

if __name__ == '__main__':
    main()
