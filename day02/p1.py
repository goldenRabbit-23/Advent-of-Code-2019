import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    program[1] = 12
    program[2] = 2

    pc = 0
    while True:
        opcode = program[pc]
        if opcode == 1:
            a, b, c = program[pc + 1:pc + 4]
            program[c] = program[a] + program[b]
        elif opcode == 2:
            a, b, c = program[pc + 1:pc + 4]
            program[c] = program[a] * program[b]
        elif opcode == 99:
            break
        pc += 4

    print(program[0])

if __name__ == '__main__':
    main()
