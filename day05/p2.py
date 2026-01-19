import sys
from intcode import IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    intcode = IntCodeComputer(program)
    intcode.run(5)

if __name__ == '__main__':
    main()
