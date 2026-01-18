import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    masses = [int(x) for x in data]
    print(sum(mass // 3 - 2 for mass in masses))

if __name__ == '__main__':
    main()
