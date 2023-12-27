import run from "aocrunner";

const parseInput = (rawInput: string) => {
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

    let rotatesAt = (sq: [string]) => {
      for (let astart = 0; astart < sq.length - 1; astart++) {
        let a = astart;
        let b = astart + 1;
        while (a >= 0 && b < sq.length && (sq[a] == sq[b])) {
          a -= 1;
          b += 1;
        }
        if (a < 0 || b >= sq.length) {
          return astart + 1; // 1 indexed
        }
      }
      return null;
    }
    ret.push([orig, rotate, rotatesAt(orig), rotatesAt(rotate)]);
  }
  return ret;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
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
  const input = parseInput(rawInput);

  return;
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
