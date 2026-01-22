import sys

W, H = 25, 6

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    layers = [data[i:i + W * H] for i in range(0, len(data), W * H)]
    rendered = [next(p for p in pos if p != '2') for pos in zip(*layers)]

    for i in range(H):
        print(''.join(' #'[int(x)] for x in rendered[i * W:(i + 1) * W]))

if __name__ == '__main__':
    main()
