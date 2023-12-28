import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const hashStr = (s: string) => {
  const hashChar = (c: string, ival : number) => {
    // Determine the ASCII code for the current character of the string.
    let ascii = c.charCodeAt(0);
    // Increase the current value by the ASCII code you just determined.
    ival += ascii;
    // Set the current value to itself multiplied by 17.
    ival *= 17;
    // Set the current value to the remainder of dividing itself by 256.
    return ival % 256;
  }

  let ret = 0;
  for (let c of s) {
    ret = hashChar(c, ret);
  }
  return ret;
}

console.assert(hashStr("H") == 200);
console.assert(hashStr("HASH") == 52);

const part1 = (rawInput: string) => {
  const input = rawInput.trim().split(",");
  let ret = 0;
  for (let ins of input) {
    let hashed = hashStr(ins);
    //console.log(ins, " became ", hashed);
    ret += hashed;
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
        input: `rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7`,
        expected: 1320,
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
