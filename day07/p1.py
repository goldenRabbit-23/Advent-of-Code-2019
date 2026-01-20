import sys
from itertools import permutations
from intcode import IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    highest_signal = 0
    for phase_settings in permutations(range(5)):
        signal = 0
        for phase in phase_settings:
            amplifier = IntCodeComputer(program[:])
            amplifier.fetch_input(phase, signal)
            signal = amplifier.run()

        highest_signal = max(highest_signal, signal)

    print(highest_signal)

if __name__ == '__main__':
    main()
