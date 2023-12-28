import run from "aocrunner";
import { assert, dir } from "console";
import exp from "constants";
import { start } from "repl";

const parseInput = (rawInput: string) => {
  let ret = [];
  for (let l of rawInput.split("\n")) {
    l = l.trim();
    ret.push(l.split(""));
  }
  return ret;
};

const threeByThree = (char: string) => {
  if (char == ".") {
    return [[false, false, false], [false, false, false], [false, false, false]];
  }

  let dir = directions(char);

  let ret = [[false, false, false], [false, true, false], [false, false, false]];
  for (let [dx, dy] of dir) {
    ret[1 + dy][1+dx] = true;
  }
  return ret;
}

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


const fixedMapAndPipe = (rawInput: string) => {
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

  let pipe = [];
  while (queue.length > 0) {
    let [x, y, dist] = queue.shift();
    if (containsMatchingSubarray(visited, [x, y])) {
      continue;
    }
    pipe.push([x, y, dist]);
    for (let [dx, dy] of directions(at(x, y))) {
      queue.push([dx + x, dy + y, dist + 1]);
    }
    visited.push([x, y]);
  };

  return [board, pipe];
}

const part1 = (rawInput: string) => {
  let [board, pipe] = fixedMapAndPipe(rawInput);

  let ret = 0;
  for (let [x, y, dist] of pipe) {
    ret = Math.max(ret, dist);
  }

  return ret;
};

const part2 = (rawInput: string) => {
  let [board, pipe] = fixedMapAndPipe(rawInput);

  let keyify = (x : number, y : number) => {
    return "" + x + "_" + y;
  }


  let targetPipes = {};
  for (let [px, py, pdist] of pipe) {
    let three = threeByThree(board[py][px]);
    for (let ty = 0; ty < 3; ty++) {
      for (let tx = 0 ; tx < 3; tx++) {
        if (three[ty][tx]) {
          targetPipes[keyify(px * 3 + tx, py * 3 + ty)] = true;
        }
      }
    }
  }
  console.log(Object.keys(targetPipes).length, pipe.length);

  let expanded = [];
  for (let y = 0; y < board.length; y++) {
    for (let z = 0; z < 3; z++) {
      let row = [];
      for (let x = 0; x < board[y].length; x++) {
        let three = threeByThree(board[y][x]);
        for (let a = 0; a < 3; a++) {
          row.push(three[z][a]);
        }
      }
      expanded.push(row);
    }
  }

  let ret = 0;

  let visited = {};
  console.log("expanded size: ", expanded[0].length, " x ", expanded.length);
  console.log("---");
  for (let ey = 0; ey < expanded.length; ey++) {
    let row = "";
    for (let ex = 0; ex < expanded[ey].length; ex++) {
      if (expanded[ey][ex] == true) {
        if (keyify(ex, ey) in targetPipes) {
          row += "!";
        } else {
          row += "*";
        }
      } else {
        if (keyify(ex, ey) in targetPipes) {
          row += "?";
        } else{ 
          row += " ";
        }
      }
    }
    console.log(row);
  }
  console.log("---");


  for (let ey = 0; ey < expanded.length; ey++) {
    for (let ex = 0; ex < expanded[ey].length; ex++) {
      // if (ex ==) // 2, 6 = first encountered one
      if (expanded[ey][ex]) {
        continue; // pipe.
      }
      if (keyify(ex, ey) in visited) {
        continue;
      }
      // unvisited, nonpipe.

      // Where we stop recursing.
      let outsides = 0;
      let numTargetpipes = 0;
      let otherpipes = 0;
      let empties = [];

      let queue = [[ex, ey]];
      while (queue.length > 0) {
        let [x, y] = queue.shift();
        if (x == 3 * 2 + 1 &&  y == 3 * 6 + 1) {
          console.log("should be targety", x, y);
        }
        if (keyify(x, y) in visited) {
          continue;
        }
        visited[keyify(x, y)] = true;

        let isOutside = (ox : number, oy : number) => {
          if (ox < 0 || oy < 0) {
            return true;
          }
          return (oy >= expanded.length || ox >= expanded[oy].length);
        }
        let isTargetPipe = (tx : number, ty : number) => {
          return (keyify(tx, ty) in targetPipes);
        }

        if (isOutside(x, y)) {
          outsides += 1;
        } else {
          if (isTargetPipe(x, y)) {
            numTargetpipes += 1;
          } else if (expanded[y][x]) {
            otherpipes += 1;
          } else {
            empties.push([x, y]);
            for (let [dx, dy] of [[-1, 0], [1, 0], [0, 1], [0, -1]]) {
              let nx = dx + x;
              let ny = dy + y;
              if (!(keyify(nx, ny) in visited)) {
                queue.push([nx, ny]);                
              }
            }
          }
        }
      }
      
      // found all adjacents.
      console.log(ex, ey, "targets: ", numTargetpipes, "others: ", otherpipes, "outsides: ", outsides);
      if (numTargetpipes >0 && otherpipes == 0 && outsides == 0) {
        for (let [goodx, goody] of empties) {
          if ((goodx - 1) % 3 == 0 && (goody - 1) % 3 == 0) {
            ret += 1;
          }
        }
      }
      console.log("Ret now: ", ret);
    }
  }


  return ret;
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
      {
        input: `...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........`,
        expected: 4,
      },
      {
        input: `.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...`,
        expected: 8,
      },
      {
        input: `FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L`,
        expected: 10,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
