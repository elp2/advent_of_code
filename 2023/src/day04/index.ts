import run from "aocrunner";

const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  
  let ret = [];
  for (let line of lines) {
    let numbers = line.split(":")[1];
    let winners = numbers.split("|")[0];
    let have = numbers.split("|")[1];

    const setify = (s: string) => {
      let ret = new Set<number>();
      for (let n of s.split(" ")) {
        n = n.trim();
        if (n != "") {
          ret.add(parseInt(n));
        }
      }
      return ret;
    }
    ret.push([setify(winners), setify(have)]);
  }
  return ret;
};

const part1 = (rawInput: string) => {
  const cards = parseInput(rawInput);

  let ret = 0;
  for (let c of cards) {
    // console.log(c);
    let winners = c[0];
    let have = c[1];
    let intersect = new Set([...winners].filter(i => have.has(i)));
    if (intersect.size > 0) {
      console.log(c, ret);
      let points = Math.pow(2, intersect.size - 1);
      console.log(points);
      ret += points;
    }
  }

  return ret;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

run({
  part1: {
    tests: [
      {
        input: `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11`,
        expected: 13,
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
  // onlyTests: true,
});
