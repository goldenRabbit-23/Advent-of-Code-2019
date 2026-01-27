import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    elements = [int(x) for x in data]
    length = len(elements)
    pattern = [0, 1, 0, -1]

    for _ in range(100):
        new_elements = []
        for i in range(length):
            total = 0
            for j in range(length):
                pattern_index = ((j + 1) // (i + 1)) % 4
                total += elements[j] * pattern[pattern_index]
            new_elements.append(abs(total) % 10)
        elements = new_elements

    print(''.join(map(str, elements[:8])))

if __name__ == '__main__':
    main()
