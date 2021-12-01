from collections import defaultdict
from copy import copy
from math import ceil, floor

def parse_item(item):
    [num, name] = item.strip().split(' ')
    return {}

def filter_zeroes(d):
    ret = defaultdict(lambda: 0)
    for k, v in d.items():
        if v != 0:
            ret[k] = v
    return ret

output_to_formula = {}
def parse_input():
    lines = open('input').readlines()
    for line in lines:
        [input_string, output_string] = line.split('=>')
        [output_number, output_chemical] = output_string.strip().split(' ')
        formula = {'num': int(output_number)}

        input_formula = defaultdict(lambda: 0)
        for inp in input_string.strip().split(','):
            [num, name] = inp.strip().split(' ')
            input_formula[name] = int(num)
        formula['inputs'] = input_formula

        output_to_formula[output_chemical] = formula

def subtract_from_extras(extras, chem, num):
    ret = num
    if chem in extras:
        from_extras = min(num, extras[chem])
        ret -= from_extras
        extras[chem] -= from_extras
    return ret

def expand_one(chem, needed, extras):
    if chem == 'ORE':
        return {chem: needed}
    formula = output_to_formula[chem]
    fnum = formula['num']
    scaling = ceil(needed / fnum)
    extra = fnum * scaling - needed
    if extra != 0:
        extras[chem] += extra
    ins = copy(formula['inputs'])
    for key in ins.keys():
        ins[key] *= scaling
        ins[key] = subtract_from_extras(extras, key, ins[key])
    return ins

def expand(chemicals):
    extras = defaultdict(lambda: 0)

    while list(chemicals.keys()) != ['ORE']:
        new = defaultdict(lambda: 0)
        for chem, num in chemicals.items():
            num = subtract_from_extras(extras, chem, num)
            expanded = expand_one(chem, num, extras)
            for key in expanded.keys():
                new[key] += expanded[key]
        print('Round! ', chemicals, '->', new)
        chemicals = new

    ret = defaultdict(lambda: 0)

    for key, value in extras.items():
        if value != 0:
            ret[key] = value
    for key, value in chemicals.items():
        if value != 0:
            ret[key] = value
    return chemicals

def part1():
    parse_input()
    chemicals = defaultdict(lambda: 0)
    chemicals['FUEL'] = 1
    while list(chemicals.keys()) != ['ORE']:
        chemicals = expand(chemicals)
        print('Expanded: ', chemicals)

# part1() # 892207

ONE_TRILLION = 1_000_000_000_000
START_FUELS = floor(ONE_TRILLION / 892207)
START_STEP = floor(START_FUELS / 2)

def part2():
    parse_input()
    fuels = START_FUELS
    step = START_STEP
    while True:
        chemicals = defaultdict(lambda: 0)
        chemicals['FUEL'] = fuels + step
        while list(chemicals.keys()) != ['ORE']:
           chemicals = expand(chemicals)
        ores = chemicals['ORE']
        if ores == ONE_TRILLION or step == 0:
            print('FUELS = ', fuels)
            break
        elif ores < ONE_TRILLION:
            fuels += step
        elif ores > ONE_TRILLION:
            step = floor(step / 2)
        print(ores - ONE_TRILLION, step)

part2() # 1935265
