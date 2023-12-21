import run from "aocrunner";

const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let instructions = lines[0];
  let network = {};
  for (let l of lines.slice(2)) {
    l = l.replace("(", "");
    l = l.replace(")", "");
    l = l.replace(" = ", " ");
    l = l.replace(",", "");
    let s = l.split(" ");
    // console.log(s);
    network[s[0]] = [s[1], s[2]];
  }
  
  return {"network": network, "instructions": instructions};
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let here = "AAA";
  let steps = 0;
  while (here != "ZZZ") {
    let dir = input.instructions[steps % input.instructions.length];
    if (dir == "L") {
      here = input.network[here][0];
    } else {
      here = input.network[here][1];
    }
    steps += 1;
  }
  //console.log(input);

  return steps;
};

function divisors(num) {
  let ret = [];
  let n = 2;
  while (true) {
    if (num == 1) {
      return ret;
    }

    if (num % n == 0) {
      ret.push(n);
      num /= n;
    } else {
      n += 1;
    }
  }
  return ret;
}

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let starters = [];
  for (let k of Object.keys(input.network)) {
    if (k[2] == "A") {
      starters.push(k);
    }
  }
  console.log(starters);
  let zpaths = [];
  for (let starter of starters) {
    let here = starter;
    let path = {};
//    path[starter] = 0;
    let steps = 0;
    while (true) {
      let dir = input.instructions[steps % input.instructions.length];
      if (dir == "L") {
        here = input.network[here][0];
      } else {
        here = input.network[here][1];
      }
      steps += 1;
      if (here[2] == "Z") {
        if (here in path) {
          console.log(here, steps);
          break; // TODO I think I have to get to the loop around.
        }
        path[here] = steps;
      }
    }
    zpaths.push(Object.values(path)[0]);
  }
  console.log(zpaths);

  let full = [];
  for (let zp of zpaths) {
    let divs = divisors(zp);
    if (full.length == 0) {
      full = divs;
    } else {
      for (let z of divs) {
        if (!full.includes(z)) {
          full.push(z);
        }
      }
    }
  }

  return full.reduce((prev, curr) => (prev * curr), 1);
};

run({
  part1: {
    tests: [
      {
        input: `LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)`,
        expected: 6,
      },
      {
        input: `RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)`,
        expected: 2,
      },      
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)`,
        expected: 6,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
