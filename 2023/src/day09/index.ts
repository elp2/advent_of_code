import run from "aocrunner";

const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let ret = [];
  for (let l of lines) {
    let nums = l.split(" ").map(x => parseInt(x));
    ret.push(nums);
  }
  return ret;
}

const deltafy = (arr: number[]) => {
  let ret = [];
  let last = null;
  for (let n of arr) {
    if (last != null) {
      ret.push(n - last);
    }
    last = n;
  }
  return ret;
};

const zeroes = (arr: number[]) => {
  for (let z of arr) {
    if (z != 0) {
      return false;
    }
  }
  return true;
}

const extrapolate = (arr: number[]) => {
  let steps = [arr];
  let here = arr;
  while (true) {
    let deltad = deltafy(here);
    if (zeroes(deltad)) {
      break;
    }
    steps.push(deltad);
    here = deltad;
  }
  let right = 0;
  for (let i = steps.length - 1; i >= 0; i--) {
    right += steps[i][steps[i].length - 1]
  }

  return right;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  let ret = 0;
  for (let l of input) {
    ret += extrapolate(l);
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
        input: `0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45`,
        expected: 114,
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
