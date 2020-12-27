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
  es = []
  maxe = None
  lines = open(fname).readlines()
  ips = lines[0].split(" ")
  assert ips[0] == "#ip"
  ip = int(ips[1])

  instructions = lines[1:]
  cpu = [0] * 6
  cpu[0] = 1 # 13443200
  print(bin(13443200))
  seens = [0] * 31
  steps = 0
  while 0 <= cpu[ip] < len(instructions):

    # 18 14280
    # 19 14279
    # 20 14279
    # 21 14279
    # 22 14277
    # 23 2
    # 24 14277
    # 25 14277
    # 26 2
    # 27 2    
    # optimize 256 loop

    # >>> [bin(b) for b in [849664,849920,850176,850432,850688]]
    # ['0b11001111011100000000', '0b11001111100000000000', '0b11001111100100000000', '0b11001111101000000000', '0b11001111101100000000']

    if cpu[ip] == 18:
      cpu[3] = cpu[3] >> 8
      cpu[ip] = 27
      


    seens[cpu[ip]] += 1
    steps += 1
    ins = instructions[cpu[ip]].split(" ")
    ins_strings = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    fns = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    if len(fns) != 16:
      raise AssertionError('not16')




    # if steps > 100000:
    #   for i, v, in enumerate(seens):
    #     print(i, v)
    #   return

    # if cpu[ip] in [6, 8, 13, 17, 27]:
    #   print("ip: ", cpu[ip], ":", "a:", cpu[0], "b:", cpu[1], "d:", cpu[3], "e:", cpu[4], "f:", cpu[5], "___steps", steps)


    if cpu[ip] == 28:      
      e = cpu[4]
      if e in es:
        print("Recursing!", es)
        print("ANSWER: ", es[-1])
        return es[-1]
      else:
        if not maxe or e > maxe:
          maxe = e
          print("New maxe: ", maxe, es)
        es.append(e)
      # print(cpu)



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
  r0s = get_es() # list(range(NUM_R0s)) + [13443200]
  assert 13443200 in r0s
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

def get_es():
  es = set()
  for b in range(0, 256):
    e = 10283511
    # b = d & 255 (0-255 inc)
    e = e + b
    e = e & 16777215
    e = e * 65899
    e = e & 16777215
    assert e not in es
    es.add(e)
  return es


def decompiled(a):
  a = a
  b = c = d = e = f = 0


  # ip 6
  d = e | 65536
  e = 10283511

  # ip 8
  b = d & 255
  e = e + b
  e = e & 16777215
  e = e * 65899
  e = e & 16777215
  b = 1 if 256 > d else 0

  # if b == 1 jump 28
  # ip = b + ip
  # ip = ip + 1
  # ip = 27

  # elif b == 0

  b = 0
  while True:
    f = b + 1
    f = f * 256
    f = 1 if f > d else 0 # When would this be true? Are there jumps in here?
    if f == 1:
      break
    b += 1

  d = b
  # jump 8


  b = 1 if e == a else 0
  if 1 == b:
    return True


  # if f == 1 jump 26
  # ip = f + ip
  # ip = ip + 1
  # ip = 25

  # elif f == 0 (
  # b = b + 1
  # ip = 17

  # d = b
  # ip = 7

  # ip = b + ip
  # ip = 5




# decompile("21.txt")
# print(part1_parallel('21.txt'))
run("21.txt")

# part 2 16763159 too high