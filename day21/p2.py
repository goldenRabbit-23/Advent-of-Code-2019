import sys
from intcode import RunStatus, IntCodeComputer

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    computer = IntCodeComputer(program)

    springscript = [
        'NOT A J',
        'NOT B T',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',  # J <- (¬A ∨ ¬B ∨ ¬C) ∧ D
        'NOT E T',
        'NOT T T',
        'OR H T',
        'AND T J',  # J <- ((¬A ∨ ¬B ∨ ¬C) ∧ D) ∧ (E ∨ H)
        'RUN'
    ]

    input_data = '\n'.join(springscript) + '\n'
    input_bytes = [ord(c) for c in input_data]
    computer.fetch_input(*input_bytes)
    status = computer.run()
    assert status == RunStatus.HALTED
    print(computer.outputs[-1])

if __name__ == '__main__':
    main()
