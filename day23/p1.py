import sys
from intcode import RunStatus, IntCodeComputer
from collections import deque

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computers = [IntCodeComputer(program) for _ in range(50)]
    queues = [deque() for _ in range(50)]

    # Boot up: provide network address
    for i, computer in enumerate(computers):
        computer.fetch_input(i)

    while True:
        for i, computer in enumerate(computers):
            # Process incoming queue
            if queues[i]:
                x, y = queues[i].popleft()
                computer.fetch_input(x, y)
            else:
                computer.fetch_input(-1)

            status = computer.run(clear_outputs=True)
            assert status == RunStatus.WAITING_FOR_INPUT
            outputs = computer.outputs

            # Process outgoing packets
            for j in range(0, len(outputs), 3):
                dst, x, y = outputs[j:j+3]
                if dst == 255:
                    print(y)
                    return
                else:
                    queues[dst].append((x, y))

if __name__ == '__main__':
    main()
