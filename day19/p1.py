import sys
from intcode import RunStatus, IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    drone = IntCodeComputer(program)
    affected = 0

    for x in range(50):
        for y in range(50):
            drone.reset()
            drone.fetch_input(x, y)
            status = drone.run()
            assert status == RunStatus.HALTED
            affected += drone.outputs[0] == 1

    print(affected)

if __name__ == '__main__':
    main()
