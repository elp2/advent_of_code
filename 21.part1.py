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


def run(fname):
  lines = open(fname).readlines()
  ips = lines[0].split(" ")
  assert ips[0] == "#ip"
  ip = int(ips[1])

  instructions = lines[1:]
  cpu = [0] * 6
  while 0 <= cpu[ip] < len(instructions):
    ins = instructions[cpu[ip]].split(" ")
    ins_strings = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    fns = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    if len(fns) != 16:
      raise AssertionError('not16')

    if cpu[ip] == 28:
      print(cpu)
    a, b, c = list(map(int, ins[1:]))
    ins_i = ins_strings.index(ins[0])
    fns[ins_i](cpu, a, b, c)

    cpu[ip] += 1

  return cpu[0]

def step(instructions, ip, cpu):
  line = instructions[cpu[ip]].strip()
  ins = line.split(" ")
  ins_strings = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
  fns = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

  if len(fns) != 16:
    raise AssertionError('not16')

    if cpu[ip] == 28:
      print(cpu, line)


  a, b, c = list(map(int, ins[1:]))
  ins_i = ins_strings.index(ins[0])
  fns[ins_i](cpu, a, b, c)

  cpu[ip] += 1

  return 0 <= cpu[ip] < len(instructions)


def part1_parallel(fname):
  steps = 0
  lines = open(fname).readlines()
  ips = lines[0].split(" ")
  assert ips[0] == "#ip"
  ip = int(ips[1])
  instructions = lines[1:]

  NUM_R0s = 2049
  r0s = list(range(NUM_R0s)) + [13443200]
  cpus = []
  for r0 in r0s:
    cpu = [0] * 6
    cpu[0] = r0
    cpus.append(cpu)
  
  steps = 0
  while True:
    if steps % 100 == 0:
      print(steps)
    steps += 1
    for i, r0 in enumerate(r0s):
      cpu = cpus[i]
      running = step(instructions, ip, cpu)
      if not running:
        print(r0, "ENDED after", steps, "!", cpu)
        return r0



def decompile(fname):
  lines = open(fname).readlines()
  ips = lines[0].split(" ")
  assert ips[0] == "#ip"
  ip = int(ips[1])
  instructions = lines[1:]

  rn = list("abcdef")
  rn[ip] = "ip"

  for line in instructions:
    ins, a, b, c = line.strip().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)

    descs = {
      "addr": lambda a, b: f"{rn[a]} + {rn[b]}",
      "addi": lambda a, b: f"{rn[a]} + {b}",
    
      "mulr": lambda a, b: f"{rn[a]} * {rn[b]}",
      "muli": lambda a, b: f"{rn[a]} * {b}",
    
      "banr": lambda a, b: f"{rn[a]} & {rn[b]}",
      "bani": lambda a, b: f"{rn[a]} & {b}",

      "borr": lambda a, b: f"{rn[a]} | {rn[b]}",
      "bori": lambda a, b: f"{rn[a]} | {b}",

      "setr": lambda a, b: f"{rn[a]}",
      "seti": lambda a, b: f"{a}",

      "gtir": lambda a, b: f"1 if {a} > {rn[b]} else 0",
      "gtri": lambda a, b: f"1 if {rn[a]} > {b} else 0",
      "gtrr": lambda a, b: f"1 if {rn[a]} > {rn[b]} else 0",

      "eqir": lambda a, b: f"1 if {a} == {rn[b]} else 0",
      "eqri": lambda a, b: f"1 if {rn[a]} == {b} else 0",
      "eqrr": lambda a, b: f"1 if {rn[a]} == {rn[b]} else 0",
    }
    print(rn[c], "=", descs[ins](a, b))


# decompile("21.txt")
print(part1_parallel('21.txt'))
# run("21.txt")
