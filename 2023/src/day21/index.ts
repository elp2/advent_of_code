import run from "aocrunner";

let DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]];

const parseInput = (rawInput: string) => {
  let board = rawInput.split("\n");

  let steps = 64;
  if (board.length < 20) {
    steps = 6;
  }
  let sy = 0;
  let sx = 0;
  for (sy = 0; sy < board.length; sy++) {
    for (sx = 0; sx < board[sy].length; sx++) {
      if (board[sy][sx] == "S") {
        console.log("found s at", sx, sy);
        return [steps, board, [sx, sy]];
        break;
      }
    }
  }
  console.log("Shouldn't happen");
};

const keyify = (x, y) => {
  return `${x}_${y}`;
};

const part1 = (rawInput: string) => {
  const [maxSteps, board, [sx, sy]] = parseInput(rawInput);

  let onBoard = (board, x, y) => {
    //console.log("ob", x, y);
    //console.log([y >= 0, y < board.length, x >= 0, x < board[y].length]);
    return (y >= 0 && y < board.length && x >= 0 && x < board[y].length);
  }


  let visitedAt = {};
  let queue = [[ sx, sy, 0 ]];
  while (queue.length > 0) {
    let [x, y, t] = queue.shift();
    // console.log([x, y]);
    if (t > maxSteps) {
      continue;
    }
    if (visitedAt[keyify(x, y)] != null) {
      continue;
    }
    if (!onBoard(board, x, y)) {
      // console.log("offboard", x, y);
      continue;
    }

    if (board[y][x] == "#") {
      visitedAt[keyify(x, y)] = "#";
      continue;
    }
    visitedAt[keyify(x, y)] = t;

    for (let [dx, dy] of DIRS) {
      let [nx, ny] = [dx + x, dy + y];
      if (onBoard(board, nx, ny) && visitedAt[keyify(nx, ny)]== null) {
        queue.push([nx, ny, t + 1]);
      }
    }
  }

  // console.log("visitedAt: ", Object.keys(visitedAt).length, visitedAt);
  let ret = 0;
  for (let v of Object.values(visitedAt)) {
    if (v % 2 == 0) {
      ret += 1;
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
        input: `...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........`,
        expected: 16,
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
