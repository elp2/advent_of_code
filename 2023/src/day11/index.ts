import run from "aocrunner";
import exp from "constants";

const parseInput = (rawInput: string, expansion: number) => {
  let lines = rawInput.split("\n");
  let noGalaxyLines = new Set<number>();
  let galaxies = [];

  let colsSeen = new Set<number>();

  let ydiff = 0;
  for (let y=0; y < lines.length; y++) {
    let row = [];
    for (let x=0; x < lines[y].length; x++) {
      if (lines[y][x] == "#") {
        row.push(x);
        colsSeen.add(x);
        galaxies.push([x, y + ydiff]);
      }
    }
    
    if (row.length == 0) {
      noGalaxyLines.add(y);
      ydiff += (expansion - 1);
    }
  }
  let xdeltas = [];
  let xd = 0;
  for (let x = 0; x < lines[0].length; x++) {
    if (!(colsSeen.has(x))) {
      xd += (expansion - 1);
    }
    xdeltas.push(xd);
  }

  let gals = [];
  console.log(xdeltas);
  for (let [gx, gy] of galaxies) {
    if (gx > 0) {
      gx += xdeltas[gx - 1];
    }
    gals.push([gx, gy]);
  }
  // console.log("GALS!", galaxies, gals);

  return [gals, noGalaxyLines];
};

function* combinationsOfLength<T>(arr: T[][], length: number, start: number = 0, combo: T[][] = []): Generator<T[][]> {
  if (combo.length === length) {
      yield combo;
      return;
  }

  for (let i = start; i < arr.length; i++) {
      yield* combinationsOfLength(arr, length, i + 1, combo.concat([arr[i]]));
  }
}
const part1 = (rawInput: string) => {
  const [galaxies, noGalaxyLines] = parseInput(rawInput, 2);

  const modMd = (g1, g2) => {
    return Math.abs(g1[1] - g2[1]) + Math.abs(g1[0] - g2[0]);
  };

  let ret = 0;
  // console.log(galaxies);
  for (let [g1, g2] of combinationsOfLength(galaxies, 2)) {
    // console.log(g1, g2);
    ret += modMd(g1, g2);
  }

  return ret;
};

const part2 = (rawInput: string) => {
  let expansion = 1000000;
  if (rawInput.split("\n")[0].length < 20) {
    expansion = 10;
  }
  console.log("Expansion: ", expansion);
  const [galaxies, noGalaxyLines] = parseInput(rawInput, expansion);

  const modMd = (g1, g2) => {
    return Math.abs(g1[1] - g2[1]) + Math.abs(g1[0] - g2[0]);
  };

  let ret = 0;
  // console.log(galaxies);
  for (let [g1, g2] of combinationsOfLength(galaxies, 2)) {
    // console.log(g1, g2);
    ret += modMd(g1, g2);
  }

  return ret;
};

run({
  part1: {
    tests: [
      {
        input: `...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....`,
        expected: 374,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [ {
        input: `...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....`,
        expected: 1030,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
