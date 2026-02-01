import sys, re
from intcode import RunStatus, IntCodeComputer
from itertools import combinations

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    program = [int(x) for x in data.split(',')]
    droid = IntCodeComputer(program)

    initial_insts = [
        'west', 'take mug', 'north', 'take easter egg', 'south', 'east',
        'south', 'east', 'north', 'take candy cane', 'south', 'west',
        'north', 'east', 'take coin', 'north', 'north', 'take hypercube',
        'south', 'east', 'take manifold', 'west', 'south', 'south',
        'east', 'take pointer', 'west', 'west', 'take astrolabe',
        'north', 'east', 'north'  # At security checkpoint
    ]

    # Execute initial gathering sequence
    droid.fetch_input(*[ord(c) for c in '\n'.join(initial_insts) + '\n'])
    droid.run(clear_outputs=True)

    # All items gathered
    items = [
        'mug', 'easter egg', 'candy cane', 'coin',
        'hypercube', 'manifold', 'pointer', 'astrolabe'
    ]

    # Try all combinations of items to pass the weight check
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            # To reset, drop everything then pick up the current combination
            commands = [f'drop {item}' for item in items] + \
                       [f'take {item}' for item in combo] + \
                       ['east']  # Attempt to pass sensor

            droid.fetch_input(*[ord(c) for c in '\n'.join(commands) + '\n'])
            droid.run(clear_outputs=True)

            output = ''.join(chr(c) for c in droid.outputs)

            # If we pass, the output won't contain the "Alert!" rejection message
            if 'Alert!' not in output:
                print(re.search(r'\d+', output).group())
                return

if __name__ == '__main__':
    main()

# A loud, robotic voice says "Analysis complete! You may proceed." and you enter the cockpit.
# Santa notices your small droid, looks puzzled for a moment, realizes what has happened, and radios your ship directly.
# "Oh, hello! You should be able to get in by typing 1077936448 on the keypad at the main airlock."

# Success with items: ('mug', 'coin', 'hypercube', 'astrolabe')