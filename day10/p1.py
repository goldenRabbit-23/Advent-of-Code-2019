import sys
from math import gcd

def main():
    with open(sys.argv[1]) as f:
        grid = f.read().strip().splitlines()

    H, W = len(grid), len(grid[0])
    asteroids = [(x, y) for y in range(H) for x in range(W) if grid[y][x] == '#']
    max_visible = 0

    for ax, ay in asteroids:
        angles = set()
        for bx, by in asteroids:
            if (ax, ay) != (bx, by):
                dx, dy = bx - ax, by - ay
                g = gcd(dx, dy)
                angles.add((dx // g, dy // g))
        max_visible = max(max_visible, len(angles))

    print(max_visible)

if __name__ == '__main__':
    main()
