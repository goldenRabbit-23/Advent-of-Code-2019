import sys
from itertools import permutations
from intcode import IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    highest_signal = 0
    for phase_settings in permutations(range(5, 10)):
        amplifiers = [IntCodeComputer(program[:]) for _ in range(5)]
        for amp, phase in zip(amplifiers, phase_settings):
            amp.fetch_input(phase)

        signal = 0
        idx = 0
        while True:
            amplifiers[idx].fetch_input(signal)
            output = amplifiers[idx].run()
            if output is None:
                break
            signal = output
            idx = (idx + 1) % 5

        highest_signal = max(highest_signal, signal)

    print(highest_signal)

if __name__ == '__main__':
    main()
