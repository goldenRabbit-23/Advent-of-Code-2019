import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    start, end = map(int, data[0].split('-'))
    valid = 0

    for num in range(start, end + 1):
        s = str(num)
        never_decreases = all(a <= b for a, b in zip(s, s[1:]))
        has_double = any(s.count(digit) >= 2 for digit in set(s))
        valid += has_double and never_decreases

    print(valid)

if __name__ == '__main__':
    main()
