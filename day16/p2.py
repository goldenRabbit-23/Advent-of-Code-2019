import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    base = [int(x) for x in data]
    L = len(base)
    offset = int(data[:7])
    M = L * 10000 - offset
    tail = [base[(offset + i) % L] for i in range(M)]

    for _ in range(100):
        new_tail = [0] * M
        suffix_sum = 0
        for i in range(M - 1, -1, -1):
            suffix_sum = (suffix_sum + tail[i]) % 10
            new_tail[i] = suffix_sum
        tail = new_tail

    print(''.join(map(str, tail[:8])))

if __name__ == '__main__':
    main()
