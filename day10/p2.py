import sys
from collections import defaultdict
from math import gcd, atan2, pi

def main():
    with open(sys.argv[1]) as f:
        grid = f.read().strip().splitlines()

    H, W = len(grid), len(grid[0])
    asteroids = [(x, y) for y in range(H) for x in range(W) if grid[y][x] == '#']
    max_visible = 0
    laser_x, laser_y = 0, 0

    for ax, ay in asteroids:
        angles = set()
        for bx, by in asteroids:
            if (ax, ay) != (bx, by):
                dx, dy = bx - ax, by - ay
                g = gcd(dx, dy)
                angles.add((dx // g, dy // g))
        if len(angles) > max_visible:
            max_visible = len(angles)
            laser_x, laser_y = ax, ay

    asteroids_by_angle = defaultdict(list)
    for bx, by in asteroids:
        if (bx, by) == (laser_x, laser_y):
            continue
        dx, dy = bx - laser_x, by - laser_y
        dist = dx * dx + dy * dy
        angle = atan2(dx, -dy) % (2 * pi)
        asteroids_by_angle[angle].append((dist, bx, by))

    for angle in asteroids_by_angle:
        asteroids_by_angle[angle].sort(reverse=True)

    sorted_angles = sorted(asteroids_by_angle.keys())

    vaporized_count = 0
    while vaporized_count < 200:
        for angle in sorted_angles:
            if asteroids_by_angle[angle]:
                _, x200, y200 = asteroids_by_angle[angle].pop()
                vaporized_count += 1
                if vaporized_count == 200:
                    print(x200 * 100 + y200)
                    return

if __name__ == '__main__':
    main()
