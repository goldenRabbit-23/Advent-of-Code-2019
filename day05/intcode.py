from enum import Enum

class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99

class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1

class IntCodeComputer:
    def __init__(self, program):
        self.program = program
        self.pc = 0

    def get_param(self, index, mode):
        # Immediate mode: the parameter is the value itself.
        if mode == ParameterMode.IMMEDIATE.value:
            return self.program[self.pc + index]
        # Position mode: the parameter is an address.
        else:
            return self.program[self.program[self.pc + index]]

    def run(self, input_val):
        while True:
            instruction = self.program[self.pc]
            opcode = instruction % 100
            modes = instruction // 100

            if opcode == Operation.ADD.value:
                val_a = self.get_param(1, modes % 10)
                val_b = self.get_param(2, (modes // 10) % 10)
                dest = self.program[self.pc + 3]
                self.program[dest] = val_a + val_b
                self.pc += 4
            elif opcode == Operation.MULTIPLY.value:
                val_a = self.get_param(1, modes % 10)
                val_b = self.get_param(2, (modes // 10) % 10)
                dest = self.program[self.pc + 3]
                self.program[dest] = val_a * val_b
                self.pc += 4
            elif opcode == Operation.INPUT.value:
                dest = self.program[self.pc + 1]
                self.program[dest] = input_val
                self.pc += 2
            elif opcode == Operation.OUTPUT.value:
                val_a = self.get_param(1, modes % 10)
                print(val_a)
                self.pc += 2
            elif opcode == Operation.JUMP_IF_TRUE.value:
                val_a = self.get_param(1, modes % 10)
                val_b = self.get_param(2, (modes // 10) % 10)
                self.pc = val_b if val_a != 0 else self.pc + 3
            elif opcode == Operation.JUMP_IF_FALSE.value:
                val_a = self.get_param(1, modes % 10)
                val_b = self.get_param(2, (modes // 10) % 10)
                self.pc = val_b if val_a == 0 else self.pc + 3
            elif opcode == Operation.LESS_THAN.value:
                val_a = self.get_param(1, modes % 10)
                val_b = self.get_param(2, (modes // 10) % 10)
                dest = self.program[self.pc + 3]
                self.program[dest] = 1 if val_a < val_b else 0
                self.pc += 4
            elif opcode == Operation.EQUALS.value:
                val_a = self.get_param(1, modes % 10)
                val_b = self.get_param(2, (modes // 10) % 10)
                dest = self.program[self.pc + 3]
                self.program[dest] = 1 if val_a == val_b else 0
                self.pc += 4
            elif opcode == Operation.HALT.value:
                break
            else:
                raise ValueError(f"Unknown opcode: {opcode}")
