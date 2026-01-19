import sys

def main():
    with open(sys.argv[1]) as f:
        data = [line.strip().split(')') for line in f]

    orbits = {orbiter: center for center, orbiter in data}

    total = 0
    for orbiter in orbits:
        while orbiter in orbits:
            orbiter = orbits[orbiter]
            total += 1

    print(total)

if __name__ == '__main__':
    main()
