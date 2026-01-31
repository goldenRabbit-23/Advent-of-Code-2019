import sys

M = 119315717514047
T = 101741582076661

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    a, b = 1, 0
    for line in data:
        if line == 'deal into new stack':
            a, b = -a % M, (-b - 1) % M
        elif line.startswith('cut '):
            n = int(line.split()[1])
            b = (b - n) % M
        elif line.startswith('deal with increment '):
            n = int(line.split()[-1])
            a, b = (a * n) % M, (b * n) % M

    A = pow(a, T, M)
    B = b * (pow(a, T, M) - 1) * pow(a - 1, -1, M) % M
    A_inv = pow(A, -1, M)

    print((2020 - B) * A_inv % M)

if __name__ == '__main__':
    main()
