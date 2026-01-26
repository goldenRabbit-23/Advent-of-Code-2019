import sys
from collections import defaultdict

ORE_LIMIT = 10**12

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

    def required_ore(fuel_amnt):
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

        return dfs('FUEL', fuel_amnt)

    lo, hi = 0, 1
    while required_ore(hi) <= ORE_LIMIT:
        hi *= 2

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if required_ore(mid) <= ORE_LIMIT:
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == '__main__':
    main()
