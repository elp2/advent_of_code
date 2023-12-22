import run from "aocrunner";
import { assert, dir } from "console";
import { start } from "repl";

const parseInput = (rawInput: string) => {
  let ret = [];
  for (let l of rawInput.split("\n")) {
    ret.push(l.split(""));
  }
  return ret;
};

const directions = (char: string) => {
  if (char == "|") {
    return [[0, 1], [0, -1]];
  } else if (char == "-") {
    return [[1, 0], [-1, 0]];
  } else if (char == "L") {
    return [[0, -1], [1, 0]];
  } else if (char == "J") {
    return [[-1, 0], [0, -1]];
  } else if (char == "7") {
    return [[0, 1], [-1, 0]];
  } else if (char == "F") {
    return [[0, 1], [1, 0]];
  } else if (char == ".") {
    return [];
  }

  console.log("Shouldn't happen[", char, "]");
  return null;
}

function containsMatchingSubarray(arrays: any[][], target: any[]): boolean {
  return arrays.some(subArray => 
      subArray.length === target.length && 
      subArray.every((element, index) => element === target[index])
  );
}

const part1 = (rawInput: string) => {
  console.log("p1");
  const board = parseInput(rawInput);

  const findStart = () => {
    for (let sy = 0; sy < board.length; sy++) {
      for (let sx = 0; sx < board[sy].length; sx++) {
        if (board[sy][sx] == "S") {
          return [sx, sy];
        }
      }
    }
    return null;
  }
  let [sx, sy] = findStart();

  const at = (x :number, y:number) => {
    if (x < 0 || x >= board[0].length) {
      return ".";
    }
    if (y < 0 || y >= board.length) {
      return ".";
    }
    return board[y][x];
  }

  const pipeFor = (sx, sy) => {
    let dirs = "";
    let up = at(sx, sy-1);
    if (containsMatchingSubarray(directions(up), ([0, 1]))) {
      dirs += "N";
    }
    let right = at(sx + 1, sy); 
    if (containsMatchingSubarray(directions(right), [-1, 0])) {
      dirs += "E";
    }
    let down = at(sx, sy + 1); 
    if (containsMatchingSubarray(directions(down), [0, -1])) {
      dirs += "S";
    }
    let left = at(sx - 1, sy); 
    if (containsMatchingSubarray(directions(left), [1, 0])) {
      dirs += "W";
    }
    console.assert(dirs.length == 2);

    if (dirs == "NS") {
      return "|";
    } else if (dirs == "EW") {
      return "-";
    } else if (dirs == "NE") {
      return "L";
    } else if (dirs == "NW") {
      return "J";
    } else if (dirs == "SW") {
      return "7";
    } else if (dirs == "ES") {
      return "F";
    }

    console.log("Unknown dir: ", dirs, up, right, down, left);
    return null;
  }

  let startPipe = pipeFor(sx, sy);
  console.log("Pipe Start = ", startPipe);
  board[sy][sx] = startPipe;

  let visited = [];
  let queue = [[sx, sy, 0]];
  let ret = 0;

  while (queue.length > 0) {
    let [x, y, dist] = queue.shift();
    if (containsMatchingSubarray(visited, [x, y])) {
      continue;
    }
    ret = Math.max(ret, dist);
    for (let [dx, dy] of directions(at(x, y))) {
      queue.push([dx + x, dy + y, dist + 1]);
    }
    visited.push([x, y]);
  };
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
        input: `.....
.S-7.
.|.|.
.L-J.
.....`,
        expected: 4,
      },
      {
        input: `..F7.
.FJ|.
SJ.L7
|F--J
LJ...`,
        expected: 8,
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
