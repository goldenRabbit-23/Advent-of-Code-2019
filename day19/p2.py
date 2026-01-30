import sys
from intcode import RunStatus, IntCodeComputer

N = 100

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    drone = IntCodeComputer(program)

    def beam(x, y):
        drone.reset()
        drone.fetch_input(x, y)
        status = drone.run()
        assert status == RunStatus.HALTED
        return drone.outputs[0]

    x, y = 0, 0
    while True:
        while beam(x, y + N - 1) == 0:
            x += 1

        if beam(x + N - 1, y) == 1:
            print(x * 10000 + y)
            return

        y += 1

if __name__ == '__main__':
    main()
