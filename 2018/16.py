def addr(cpu, a, b, c):
  cpu[c] = cpu[a] + cpu[b]
  return cpu

def addi(cpu, a, b, c):
  cpu[c] = cpu[a] + b
  return cpu

def mulr(cpu, a, b, c):
  cpu[c] = cpu[a] * cpu[b]
  return cpu

def muli(cpu, a, b, c):
  cpu[c] = cpu[a] * b
  return cpu

def banr(cpu, a, b, c):
  cpu[c] = cpu[a] & cpu[b]
  return cpu

def bani(cpu, a, b, c):
  cpu[c] = cpu[a] & b
  return cpu

def borr(cpu, a, b, c):
  cpu[c] = cpu[a] | cpu[b]
  return cpu

def bori(cpu, a, b, c):
  cpu[c] = cpu[a] | b
  return cpu

def setr(cpu, a, b, c):
  cpu[c] = cpu[a]
  return cpu

def seti(cpu, a, b, c):
  cpu[c] = a
  return cpu

def gtir(cpu, a, b, c):
  if a > cpu[b]:
    cpu[c] = 1
  else:
    cpu[c] = 0
  return cpu

def gtri(cpu, a, b, c):
  if cpu[a] > b:
    cpu[c] = 1
  else:
    cpu[c] = 0
  return cpu

def gtrr(cpu, a, b, c):
  if cpu[a] > cpu[b]:
    cpu[c] = 1
  else:
    cpu[c] = 0
  return cpu

def eqir(cpu, a, b, c):
  if a == cpu[b]:
    cpu[c] = 1
  else:
    cpu[c] = 0
  return cpu

def eqri(cpu, a, b, c):
  if cpu[a] == b:
    cpu[c] = 1
  else:
    cpu[c] = 0
  return cpu

def eqrr(cpu, a, b, c):
  if cpu[a] == cpu[b]:
    cpu[c] = 1
  else:
    cpu[c] = 0
  return cpu


def parse_before_after(lines):
  if lines[0] == '\n':
    return None

  if not lines[0].startswith('Before'):
    print(lines)
    raise AssertionError('not before')

  # Before: [0, 1, 2, 2]
  before = eval(lines[0][8:])
  op = lines[1].split(' ')
  after = eval(lines[2][8:])
  return [before, op, after]


def part1():
  lines = open('16.txt').readlines()
  three_plus = 0
  i = 0
  while True:
    before_after = parse_before_after(lines[i:i+3])
    if not before_after:
      break
    [before, op, after] = before_after
    fns = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    if len(fns) != 16:
      raise AssertionError('not16')
    num_behave = 0
    for f in fns:
      executed = f(before[:], int(op[1]), int(op[2]), int(op[3]))
      if after == executed:
        num_behave += 1
    if num_behave >= 3:
      three_plus += 1
    i += 4
  print(three_plus)

part1()


def refine_func_map(fm):
  """Returns a mapping of opcode to my internal list of functions."""
  times = 0
  while times < 20:
    times += 1
    for fi in fm.keys():
      poss = fm[fi]
      if len(poss) == 1:
        [to_kill] = poss
        for fo in fm.keys():
          if to_kill in fm[fo] and len(fm[fo]) != 1:
            fm[fo].remove(to_kill)

  ret = {}
  for k in fm.keys():
    if len(fm[k]) != 1:
      raise AssertionError('too long')
    ret[fm[k][0]] = k
  return ret


def part2():
  lines = open('16.txt').readlines()

  func_map = {}
  for fi in range(0, 16):
    func_map[fi] = list(range(0, 16))

  fns = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
  if len(fns) != 16:
    raise AssertionError('not16')

  i = 0
  while True:
    before_after = parse_before_after(lines[i:i + 3])
    if not before_after:
      break
    [before, op, after] = before_after
    for fi in range(len(fns)):
      f = fns[fi]
      executed = f(before[:], int(op[1]), int(op[2]), int(op[3]))
      if after != executed:
        code = int(op[0])
        if code in func_map[fi]:
          func_map[fi].remove(code)
    i += 4

  print(func_map)
  fm = refine_func_map(func_map)
  print(fm)

  while lines[i] == '\n':
    i += 1

  cpu = [0, 0, 0, 0]
  while i < len(lines):
    line = lines[i]
    [code, a, b, c] = line.split(' ')
    fn = fns[fm[int(code)]]
    cpu = fn(cpu, int(a), int(b), int(c))
    print(line.strip(), fn, cpu)
    i += 1
  print(cpu, i)


part2()
