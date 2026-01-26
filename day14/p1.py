import sys
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    dependencies = {}
    for line in data:
        inputs, output = line.split(' => ')
        output_qty, output_chem = output.split()
        inputs_list = []
        for inp in inputs.split(', '):
            inp_qty, inp_chem = inp.split()
            inputs_list.append((int(inp_qty), inp_chem))
        dependencies[output_chem] = (int(output_qty), inputs_list)

    surplus = defaultdict(int)
    def dfs(chem, qty_needed):
        if chem == 'ORE':
            return qty_needed

        if surplus[chem] >= qty_needed:
            surplus[chem] -= qty_needed
            return 0

        qty_needed -= surplus[chem]
        surplus[chem] = 0
        output_qty, inputs = dependencies[chem]
        batches = (qty_needed + output_qty - 1) // output_qty
        total_ore = 0

        for inp_qty, inp_chem in inputs:
            total_ore += dfs(inp_chem, inp_qty * batches)

        surplus[chem] += batches * output_qty - qty_needed

        return total_ore

    print(dfs('FUEL', 1))

if __name__ == '__main__':
    main()
