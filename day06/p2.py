import sys

def main():
    with open(sys.argv[1]) as f:
        data = [line.strip().split(')') for line in f]

    orbits = {orbiter: center for center, orbiter in data}

    dist_you = {}
    cur = orbits['YOU']
    d = 0
    while cur in orbits:
        dist_you[cur] = d
        cur = orbits[cur]
        d += 1
    dist_you[cur] = d

    cur = orbits['SAN']
    d = 0
    while cur not in dist_you:
        cur = orbits[cur]
        d += 1

    print(d + dist_you[cur])

if __name__ == '__main__':
    main()
