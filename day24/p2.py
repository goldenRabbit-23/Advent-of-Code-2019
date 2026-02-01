import sys
from collections import defaultdict
from copy import deepcopy

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    grid = [list(line) for line in data]
    H, W = len(grid), len(grid[0])
    levels = defaultdict(lambda: [['.' for _ in range(W)] for _ in range(H)])
    levels[0] = grid

    def get_neighbors(level, r, c):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) == (2, 2):  # Center tile, recurse inward
                inner_points = []
                if   dr == 1:  inner_points = [(0, i) for i in range(5)]  # Down into top of inner
                elif dr == -1: inner_points = [(4, i) for i in range(5)]  # Up into bottom of inner
                elif dc == 1:  inner_points = [(i, 0) for i in range(5)]  # Right into left of inner
                elif dc == -1: inner_points = [(i, 4) for i in range(5)]  # Left into right of inner
                neighbors.extend((level + 1, ir, ic) for ir, ic in inner_points)
            elif 0 <= nr < H and 0 <= nc < W:  # Normal neighbor
                neighbors.append((level, nr, nc))
            else:  # Outside edge, recurse outward
                outer_r, outer_c = 2 + dr, 2 + dc
                neighbors.append((level - 1, outer_r, outer_c))
        return neighbors

    for _ in range(200):
        new_levels = deepcopy(levels)
        min_level, max_level = min(levels.keys()), max(levels.keys())

        # Check one level beyond current bounds as bugs can spread out
        for level in range(min_level - 1, max_level + 2):
            for r in range(H):
                for c in range(W):
                    if (r, c) == (2, 2): continue  # Center is grid-within-grid

                    bugs = sum(
                        levels[l][nr][nc] == '#'
                        for l, nr, nc in get_neighbors(level, r, c)
                    )

                    if levels[level][r][c] == '#' and bugs != 1:
                        new_levels[level][r][c] = '.'
                    elif levels[level][r][c] == '.' and bugs in (1, 2):
                        new_levels[level][r][c] = '#'

        levels = new_levels

    print(sum(row.count('#') for grid in levels.values() for row in grid))

if __name__ == '__main__':
    main()
