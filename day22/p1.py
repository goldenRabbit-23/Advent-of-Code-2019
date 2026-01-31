import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    deck = list(range(10007))
    for line in data:
        if line == 'deal into new stack':
            deck.reverse()
        elif line.startswith('cut '):
            n = int(line.split()[1])
            deck = deck[n:] + deck[:n]
        elif line.startswith('deal with increment '):
            n = int(line.split()[-1])
            new_deck = [0] * len(deck)
            for i, card in enumerate(deck):
                new_deck[(i * n) % len(deck)] = card
            deck = new_deck

    print(deck.index(2019))

if __name__ == '__main__':
    main()
