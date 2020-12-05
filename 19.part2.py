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


def part1(fname):
  lines = open(fname).readlines()
  ips = lines[0].split(" ")
  assert ips[0] == "#ip"
  ip = int(ips[1])

  instructions = lines[1:]
  cpu = [0] * 6
  cpu[0] = 1
  while 0 <= cpu[ip] < len(instructions):
    ins = instructions[cpu[ip]].split(" ")
    ins_strings = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    fns = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    if len(fns) != 16:
      raise AssertionError('not16')

    a, b, c = list(map(int, ins[1:]))
    ins_i = ins_strings.index(ins[0])
    fns[ins_i](cpu, a, b, c)

    cpu[ip] += 1

  return cpu[0]


# assert part1('19.sample') == 6
# print('Calculated SAMPLE')
print(part1('19.txt'))

