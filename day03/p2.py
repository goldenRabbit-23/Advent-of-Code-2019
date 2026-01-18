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
        x, y, step = 0, 0, 0
        points = {}
        for move in moves.split(','):
            d, dist = move[0], int(move[1:])
            for _ in range(dist):
                dx, dy = DELTA[d]
                x, y = x + dx, y + dy
                step += 1
                if (x, y) not in points:
                    points[(x, y)] = step
        return points

    path1 = get_points(data[0])
    path2 = get_points(data[1])

    print(min(path1[p] + path2[p] for p in path1.keys() & path2.keys()))

if __name__ == '__main__':
    main()
