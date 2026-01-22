import sys

W, H = 25, 6

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    layers = [data[i:i + W * H] for i in range(0, len(data), W * H)]
    target_layer = min(layers, key=lambda x: x.count('0'))
    print(target_layer.count('1') * target_layer.count('2'))

if __name__ == '__main__':
    main()
