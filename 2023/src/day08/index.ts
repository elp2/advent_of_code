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

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
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
      // {
      //   input: ``,
      //   expected: "",
      // },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
