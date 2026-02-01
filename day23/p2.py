import sys
from intcode import RunStatus, IntCodeComputer
from collections import deque

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computers = [IntCodeComputer(program) for _ in range(50)]
    queues = [deque() for _ in range(50)]
    nat = None
    last_nat_y = None

    # Boot up: provide network address
    for i, computer in enumerate(computers):
        computer.fetch_input(i)

    while True:
        is_idle = True

        for i, computer in enumerate(computers):
            # Process incoming queue
            if queues[i]:
                is_idle = False
                x, y = queues[i].popleft()
                computer.fetch_input(x, y)
            else:
                computer.fetch_input(-1)

            status = computer.run(clear_outputs=True)
            assert status == RunStatus.WAITING_FOR_INPUT
            outputs = computer.outputs

            # Process outgoing packets
            for j in range(0, len(outputs), 3):
                is_idle = False
                dst, x, y = outputs[j:j+3]
                if dst == 255:
                    nat = (x, y)
                else:
                    queues[dst].append((x, y))

        # Check network idleness (empty queues and no packet activity this cycle)
        if is_idle and nat:
            x, y = nat
            if y == last_nat_y:
                print(y)
                return
            queues[0].append(nat)
            last_nat_y = y

if __name__ == '__main__':
    main()
