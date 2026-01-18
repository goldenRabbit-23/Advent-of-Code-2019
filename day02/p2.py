import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]

    def run(program):
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

    for noun in range(100):
        for verb in range(100):
            test_program = program[:]
            test_program[1] = noun
            test_program[2] = verb
            run(test_program)

            if test_program[0] == 19690720:
                print(100 * noun + verb)
                return

if __name__ == '__main__':
    main()
