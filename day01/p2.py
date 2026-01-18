import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    masses = [int(x) for x in data]
    total = 0
    for mass in masses:
        fuel = mass // 3 - 2
        while fuel > 0:
            total += fuel
            fuel = fuel // 3 - 2

    print(total)

if __name__ == '__main__':
    main()
