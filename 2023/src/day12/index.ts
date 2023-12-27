import run from "aocrunner";
import exp from "constants";

const parseInput = (rawInput: string) => {
  let ret = [];
  for (let l of rawInput.split("\n")) {
    ret.push(possibilities(l));
  }
  return ret;
};

const possibilities = (line: string) => {
  let poss = [];
  let nums = line.split(" ")[1].split(",").map(x => parseInt(x));
  let map = line.split(" ")[0];
  let groups = map.split(".");
  groups = groups.filter(x => x.length > 0);

  return [groups, nums];
};

const advance = (potentials : [string], pi : number, pii : number, expected : [number], ei : number) => {
  // console.log("advance: ", pi, pii, ei);

  if (ei == expected.length) {
    for (let pix = pi; pix < potentials.length; pix++) {
      for (let pixi = (pix ==pi ? pii : 0); pixi < potentials[pix].length; pixi++) {
        if (potentials[pix][pixi] == "#") {
          // console.log("remainder had a #");
          return 0;
        }
      }
    }

    // console.log("Ended here!");
    return 1;
  }

  if (pi == potentials.length) {
    return 0;
  }

  if (pii >= potentials[pi].length) {
    // console.log("atend, advancing");
    return advance(potentials, pi + 1, 0, expected, ei);
  }

  let ret = 0;
  let here = potentials[pi][pii];
  let afteri = pii + expected[ei];
  if (afteri == potentials[pi].length) {
    ret += advance(potentials, pi + 1, 0, expected, ei + 1);
  } else if (potentials[pi][afteri] == "?") {
    // Optional, so we can skip.
    ret += advance(potentials, pi, afteri + 1, expected, ei + 1);
  } else {
    // "#", which can't be skipped and must have been included in this expcted.
  }

  if (here == "?") {
    ret += advance(potentials, pi, pii + 1, expected, ei);
  }


  return ret;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let ret = 0;
  for (let [possibilities, expected] of input) {
    console.log(possibilities, expected);
    ret += advance(possibilities, 0, 0, expected, 0);
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
        input: `? 1`,
        expected: 1,
      },      

      {
        input: `# 1`,
        expected: 1,
      },      

      {
        input: `?? 2`,
        expected: 1,
      },      

      {
        input: `??? 2`,
        expected: 2,
      },      

      {
        input: `?#? 2`,
        expected: 2,
      },      

      {
        input: `?#? 3`,
        expected: 1,
      },      

      {
        input: `????? 2,2`,
        expected: 1,
      },      


      {
        input: `???.### 1,1,3`,
        expected: 1,
      },      
      {
        input: `.??..??...?##. 1,1,3`,
        expected: 4,
      },
      {
        input: `???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1`,
        expected: 21,
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