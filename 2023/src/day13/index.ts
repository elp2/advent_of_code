import run from "aocrunner";

const parseInput = (rawInput: string, expectedDelta: number) => {
  let ret = [];

  let squares = rawInput.split("\n\n");
  for (let s of squares) {
    let orig = s.split("\n");
    let rotate = [];
    for (let x = 0; x < orig[0].length; x++) {
      let row = "";
      for (let y = 0; y < orig.length; y++) {
        row += orig[y][x];
      }
      rotate.push(row);
    }
    let getDelta = (a, b) => {
      let ret = 0;
      for (let i = 0; i < a.length; i++) {
        if (a[i] != b[i]) {
          ret += 1;
        }
      }
      return ret;
    };
    let rotatesAt = (sq: [string], expectedDelta : number) => {
      for (let astart = 0; astart < sq.length - 1; astart++) {
        let delta = 0;
        let a = astart;
        let b = astart + 1;

        while (a >= 0 && b < sq.length) {
          delta += getDelta(sq[a], sq[b]);
          if (delta > expectedDelta) {
            break;
          }
          a -= 1;
          b += 1;
        }
        if ((a < 0 || b >= sq.length) && expectedDelta == delta) {
          return astart + 1; // 1 indexed
        }
      }
      return null;
    }
    ret.push([orig, rotate, rotatesAt(orig, expectedDelta), rotatesAt(rotate, expectedDelta)]);
  }
  return ret;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput, 0);
  // console.log(input);

  let ret = 0;
  for (let [o, r, oi, ri] of input) {
    if (oi != null) {
      ret += oi * 100;
    } else if (ri != null) {
      ret += ri;
    } else {
      console.log("???");
    }
  } 

  return ret;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput, 1);
  // console.log(input);

  let ret = 0;
  for (let [o, r, oi, ri] of input) {
    if (oi != null) {
      ret += oi * 100;
    } else if (ri != null) {
      ret += ri;
    } else {
      console.log("???");
    }
  } 

  return ret;
};

run({
  part1: {
    tests: [
  {
    input: `#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#`,
    expected: 405,
  },
    ],
    solution: part1,
  },
  part2: {
    tests: [
  {
    input: `#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#`,
    expected: 400,
  },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
