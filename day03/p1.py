import sys

DELTA = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    def get_points(moves):
        x, y, points = 0, 0, set()
        for move in moves.split(','):
            d, dist = move[0], int(move[1:])
            for _ in range(dist):
                dx, dy = DELTA[d]
                x, y = x + dx, y + dy
                points.add((x, y))
        return points

    intersections = get_points(data[0]) & get_points(data[1])
    print(min(abs(x) + abs(y) for x, y in intersections))

if __name__ == '__main__':
    main()
