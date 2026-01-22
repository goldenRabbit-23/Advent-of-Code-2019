import sys
from intcode import IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computer = IntCodeComputer(program)
    computer.fetch_input(2)
    computer.run()

if __name__ == '__main__':
    main()
