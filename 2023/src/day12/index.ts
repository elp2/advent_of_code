import run from "aocrunner";
import exp from "constants";

const parseInput = (rawInput: string, unfold : boolean) => {
  let ret = [];
  for (let l of rawInput.split("\n")) {
    ret.push(possibilities(l, unfold));
  }
  return ret;
};

const possibilities = (line: string, unfold: boolean) => {
  let poss = [];
  let nums = line.split(" ")[1].split(",").map(x => parseInt(x));
  if (unfold) {
    nums = [].concat(...Array(5).fill(nums));
    //console.log(nums);    
  }

  let map = line.split(" ")[0];
  let mapunfolded = map;
  if (unfold) {
    for (let t = 0; t < 5; t++) {
      if (t >= 1) {
        mapunfolded += "?" + map;
      }
    }
    // console.log(mapunfolded);
  }
  let groups = mapunfolded.split(".");
  groups = groups.filter(x => x.length > 0);

  return [groups, nums];
};

const advance = (potentials : [string], pi : number, pii : number, expected : [number], ei : number, cache) => {
  const getKey = (a, b, c) => {
    return "" + a + "_" + b + "_" + c;
  }
  let key = getKey(pi, pii, ei);
  // console.log("advance: ", pi, pii, ei);
  if (key in cache) {
    return cache[key];
  }

  if (ei == expected.length) {
    for (let pix = pi; pix < potentials.length; pix++) {
      for (let pixi = (pix ==pi ? pii : 0); pixi < potentials[pix].length; pixi++) {
        if (potentials[pix][pixi] == "#") {
          // console.log("remainder had a #");
          cache[key] = 0;
          return cache[key];
        }
      }
    }

    // console.log("Ended here!");
    cache[key] = 1;
    return cache[key];
  }

  if (pi == potentials.length) {
    cache[key] = 0;
    return cache[key];
  }

  if (pii >= potentials[pi].length) {
    // console.log("atend, advancing");
    return advance(potentials, pi + 1, 0, expected, ei, cache);
  }

  let ret = 0;
  let here = potentials[pi][pii];
  let afteri = pii + expected[ei];
  if (afteri == potentials[pi].length) {
    ret += advance(potentials, pi + 1, 0, expected, ei + 1, cache);
  } else if (potentials[pi][afteri] == "?") {
    // Optional, so we can skip.
    ret += advance(potentials, pi, afteri + 1, expected, ei + 1, cache);
  } else {
    // "#", which can't be skipped and must have been included in this expcted.
  }

  if (here == "?") {
    ret += advance(potentials, pi, pii + 1, expected, ei, cache);
  }
  cache[key] = ret;
  return cache[key];
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput, false);
  let ret = 0;
  for (let [possibilities, expected] of input) {
    //console.log(possibilities, expected);
    ret += advance(possibilities, 0, 0, expected, 0, {});
  }
  return ret;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput, true);
  let ret = 0;
  let i = 0;
  for (let [possibilities, expected] of input) {
    console.log(i, input.length);
    i += 1;
    // console.log(possibilities, expected);
    ret += advance(possibilities, 0, 0, expected, 0, {});
  }
  return ret;
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
      {
        input: `???.### 1,1,3`,
        expected: 1,
      },      
      {
        input: `.??..??...?##. 1,1,3`,
        expected: 16384,
      },

      {
        input: `???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1`,
        expected: 525152,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});