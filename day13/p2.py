import sys
from intcode import RunStatus, IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computer = IntCodeComputer(program)
    status = computer.run()
    assert status == RunStatus.HALTED

    ball_x = paddle_x = 0

    # Process initial state to find positions
    for i in range(0, len(computer.outputs), 3):
        x, y, z = computer.outputs[i:i+3]
        if z == 3: paddle_x = x
        elif z == 4: ball_x = x

    computer.reset()
    computer.memory[0] = 2
    score = 0
    status = None

    while status != RunStatus.HALTED:
        # Simple AI: move paddle towards ball
        input_value = (ball_x > paddle_x) - (ball_x < paddle_x)
        computer.fetch_input(input_value)
        status = computer.run(clear_outputs=True)

        for x, y, z in zip(computer.outputs[0::3], computer.outputs[1::3], computer.outputs[2::3]):
            if (x, y) == (-1, 0):
                score = z
            elif z == 3:
                paddle_x = x
            elif z == 4:
                ball_x = x

    print(score)

if __name__ == '__main__':
    main()
