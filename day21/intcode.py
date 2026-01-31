from enum import Enum
from collections import defaultdict

class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE_OFFSET = 9
    HALT = 99

class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class RunStatus(Enum):
    OUTPUT = 1
    WAITING_FOR_INPUT = 2
    HALTED = 3

class IntCodeComputer:
    def __init__(self, program):
        self.program = program
        self.memory = defaultdict(int, enumerate(self.program))
        self.pc = 0
        self.relative_base = 0
        self.input_values = []
        self.input_index = 0
        self.outputs = []

    def reset(self):
        self.memory = defaultdict(int, enumerate(self.program))
        self.pc = 0
        self.relative_base = 0
        self.input_values = []
        self.input_index = 0
        self.outputs = []

    def fetch_input(self, *values_to_fetch):
        self.input_values.extend(values_to_fetch)

    def get_value(self, index, mode):
        val_at_pc = self.memory[self.pc + index]
        if mode == ParameterMode.POSITION.value:
            return self.memory[val_at_pc]
        elif mode == ParameterMode.IMMEDIATE.value:
            return val_at_pc
        elif mode == ParameterMode.RELATIVE.value:
            return self.memory[self.relative_base + val_at_pc]
        raise ValueError(f"Unknown parameter mode: {mode}")

    def get_address(self, index, mode):
        val_at_pc = self.memory[self.pc + index]
        if mode == ParameterMode.POSITION.value:
            return val_at_pc
        elif mode == ParameterMode.RELATIVE.value:
            return self.relative_base + val_at_pc
        raise ValueError(f"Unknown parameter mode: {mode}")

    def run(self, *, stop_on_output=False, max_outputs=None, clear_outputs=True):
        if clear_outputs:
            self.outputs = []

        while True:
            instruction = self.memory[self.pc]
            opcode = instruction % 100
            modes = instruction // 100

            if opcode == Operation.ADD.value:
                val_a = self.get_value(1, modes % 10)
                val_b = self.get_value(2, (modes // 10) % 10)
                dest = self.get_address(3, (modes // 100) % 10)
                self.memory[dest] = val_a + val_b
                self.pc += 4

            elif opcode == Operation.MULTIPLY.value:
                val_a = self.get_value(1, modes % 10)
                val_b = self.get_value(2, (modes // 10) % 10)
                dest = self.get_address(3, (modes // 100) % 10)
                self.memory[dest] = val_a * val_b
                self.pc += 4

            elif opcode == Operation.INPUT.value:
                if self.input_index >= len(self.input_values):
                    return RunStatus.WAITING_FOR_INPUT

                dest = self.get_address(1, modes % 10)
                self.memory[dest] = self.input_values[self.input_index]
                self.input_index += 1
                self.pc += 2

            elif opcode == Operation.OUTPUT.value:
                val_a = self.get_value(1, modes % 10)
                self.pc += 2
                self.outputs.append(val_a)

                if stop_on_output:
                    return RunStatus.OUTPUT
                if max_outputs is not None and len(self.outputs) >= max_outputs:
                    return RunStatus.OUTPUT

            elif opcode == Operation.JUMP_IF_TRUE.value:
                val_a = self.get_value(1, modes % 10)
                val_b = self.get_value(2, (modes // 10) % 10)
                self.pc = val_b if val_a != 0 else self.pc + 3

            elif opcode == Operation.JUMP_IF_FALSE.value:
                val_a = self.get_value(1, modes % 10)
                val_b = self.get_value(2, (modes // 10) % 10)
                self.pc = val_b if val_a == 0 else self.pc + 3

            elif opcode == Operation.LESS_THAN.value:
                val_a = self.get_value(1, modes % 10)
                val_b = self.get_value(2, (modes // 10) % 10)
                dest = self.get_address(3, (modes // 100) % 10)
                self.memory[dest] = 1 if val_a < val_b else 0
                self.pc += 4

            elif opcode == Operation.EQUALS.value:
                val_a = self.get_value(1, modes % 10)
                val_b = self.get_value(2, (modes // 10) % 10)
                dest = self.get_address(3, (modes // 100) % 10)
                self.memory[dest] = 1 if val_a == val_b else 0
                self.pc += 4

            elif opcode == Operation.RELATIVE_BASE_OFFSET.value:
                val_a = self.get_value(1, modes % 10)
                self.relative_base += val_a
                self.pc += 2

            elif opcode == Operation.HALT.value:
                return RunStatus.HALTED

            else:
                raise ValueError(f"Unknown opcode: {opcode}")
