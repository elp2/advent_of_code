import run from "aocrunner";
import { assert } from "console";

const keyify = (x, y) => {
  return "" + x + "_" + y;
}

const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let rocks = {};
  for (let y = 0; y < lines.length; y++) {
    for (let x = 0; x < lines[y].length; x++) {
      if (lines[y][x] == "O" || lines[y][x] == "#") {
        rocks[keyify(x, y)] = lines[y][x];
      }
    }
  }

  return [rocks, lines[0].length, lines.length];
};

const printRocks = (rocks, wx, wy) => {
  console.log(getRocksString(rocks, wx, wy));
};

const getRocksString = (rocks, wx, wy) => {
  let ret = "";
  for (let y = 0; y < wy; y++) {
    let row = "";
    for (let x = 0; x < wx; x++) {
      let k = keyify(x, y);
      if (k in rocks) {
        row += rocks[k];
      }
      else {
        row += ".";
      }
    }
    ret += row + "\n";
  }
  return ret;
};

let shiftRowCol = (rocks, shifted, dx, dy, sx, sy, wx, wy) => {
  let x = sx;
  let y = sy;

  let seenRoundRocks = 0;
  while (x >= 0 && x < wx && y >= 0 && y < wy) {
    let here = rocks[keyify(x, y)];
    // console.log(x, y, here);
    if (here == "#") {
      shifted[keyify(x, y)] = "#";
      let hx = x - dx;
      let hy = y - dy;
      for (let srr = 0; srr < seenRoundRocks; srr++) {
        shifted[keyify(hx, hy)] = "O";
        hx -= dx;
        hy -= dy;
      }
      seenRoundRocks = 0;
    } else if (here == "O") {
      seenRoundRocks += 1;
    } else {
      // empty, do nothing.
    }

    x += dx;
    y += dy;
  }

  // Add any extras that might be against the end;
  let hx = x - dx;
  let hy = y - dy;
  for (let srr = 0; srr < seenRoundRocks; srr++) {
    shifted[keyify(hx, hy)] = "O";
    hx -= dx;
    hy -= dy;
  }
  return shifted;
};

const shiftRocks = (rocks, dir, wx, wy) => {
  let dx = 0;
  let dy = 0;
  let sx = 0;
  let sy = 0;
  if (dir == "N") {
    dy = -1;
    sy = wy - 1;
  } else if (dir == "E") {
    dx = 1;
    sx = 0;
  } else if (dir == "S") {
    dy = 1;
    sy = 0;
  } else if (dir == "W") {
    dx = -1;
    sx = wx - 1;
  }
  let shifted = {};

  if (dy != 0) {
    for (let x = 0; x < wx; x++) {
      shiftRowCol(rocks, shifted, dx, dy, x, sy, wx, wy);
    }
  } else {
    for (let y = 0; y < wy; y++) {
      shiftRowCol(rocks, shifted, dx, dy, sx, y, wx, wy);
    }
  }
  return shifted;
}

const calculateSupport = (rocks, wx, wy) => {
  let ret = 0;
  for (let x = 0; x < wx; x++) {
    for (let y = 0; y < wy; y++) {
      if (keyify(x, y) in rocks) {
        if (rocks[keyify(x, y)] == "O") {
          ret += wy - y;
        }
      }
    }
  }
  return ret;
}

const part1 = (rawInput: string) => {
  const [rocks, wx, wy] = parseInput(rawInput);
  // printRocks(rocks, wx, wy);
  // console.log("got input");
  let shifted = shiftRocks(rocks, "N", wx, wy);
  // printRocks(shifted, wx, wy);

  return calculateSupport(shifted, wx, wy);
};

const part2 = (rawInput: string) => {
  let [rocks, wx, wy] = parseInput(rawInput);

  const totalTimes = 1000000000;

  let t = 0;
  let seens = {};
  let dirs = ["N", "W", "S", "E"];
  while (t < totalTimes) {
    for (let dir of dirs) {
      rocks = shiftRocks(rocks, dir, wx, wy);
    }
    if (t % 1000 == 0) {
      console.log(t);
    }
    let here = getRocksString(rocks, wx, wy);
    // console.log(t, " support = ", calculateSupport(rocks, wx, wy));
    if (here in seens) {
      let delta = t - seens[here];
      console.log("Found previous for t = ", t, " at ", seens[here], " d = ", delta, calculateSupport(rocks, wx, wy));
      while(t + delta < totalTimes) {
        t += delta;
      }
      console.log("Now at ", t);
    } else {
      seens[here] = t;
    }
    t += 1;
  }

  return calculateSupport(rocks, wx, wy);
};

run({
  part1: {
    tests: [
{
  input: `O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....`,
  expected: 136,
},
    ],
    solution: part1,
  },
  part2: {
    tests: [
{
  input: `O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....`,
  expected: 64,
},
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
