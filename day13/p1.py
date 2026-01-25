import sys
from intcode import RunStatus, IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computer = IntCodeComputer(program)
    status = computer.run()
    assert status == RunStatus.HALTED
    print(computer.outputs[2::3].count(2))

if __name__ == '__main__':
    main()
