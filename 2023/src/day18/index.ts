import run from "aocrunner";
import { parse } from "path";

const parseInput = (rawInput: string) => {
  let ret = [];
  for (let l of rawInput.split("\n")) {
    let [dir, length, color] = l.split(" ");
    color = color.substring(2, color.length - 1);
    ret.push([dir, parseInt(length), color]);
  }
  return ret;
};

const keyify = (pos) => {
  let [x, y] = pos;
  return `${x}_${y}`;
}

const DIRS = {"U": [0, -1], "L": [-1, 0], "R": [1, 0], "D": [0, 1]};

const arounds = (x, y) => {
  let ret = [];
  for (let [dx, dy] of [[0, -1], [1, 0], [0, 1], [-1, 0]]) {
    ret.push([x + dx, y + dy]);
  }
  return ret;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  let holes = {};
  let pos = [0, 0];
  holes[keyify(pos)] = true;
  
  let minX = 10000;
  let maxX = -1000;
  let minY = 1000;
  let maxY = -1000;

  for (let [dir, length, color] of input) {
    let [dx, dy] = DIRS[dir];
    let [x, y] = pos;
    for (let i = 0; i < length; i++) {
      x += dx;
      y += dy;
      pos = [x, y];
      minX = Math.min(x, minX);
      minY = Math.min(y, minY);
      maxX = Math.max(x, maxX);
      maxY = Math.max(y, maxY);

      holes[keyify(pos)] = true;
    }
  }
  console.log(Object.keys(holes).length, minX, minY, maxX, maxY);

  let ret = Object.keys(holes).length;

  let isOutside = (x, y) => {
    return y > maxY || y < minY || x > maxX || x < minX;
  }

  for (let y = minY; y <= maxY; y++) {
    for (let x = minX; x <= maxX; x++) {
      if (holes[keyify([x, y])] != null) {
        continue;
      }
      console.log("Starting at ", x, y);

      let queue = [[x, y]];
      let visited = {};
      let insideHole = true;
      while (queue.length > 0) {
        let [qx, qy] = queue.shift();
        if (keyify([qx, qy]) in visited) {
          continue;
        }
        visited[keyify([qx, qy])] = true;
        for (let [ax, ay] of arounds(qx, qy)) {
          // console.log("Around ", ax, ay);
          if (isOutside(ax, ay)) {
            // console.log(ax, ay, "is outside!");
            insideHole = false;
          } else {
            if (holes[keyify([ax, ay])] != true) {
              // console.log("pushing ", ax, ay);
              queue.push([ax, ay]);
            } else {
              // console.log(ax, ay, "is already a hole!");
            }
          }
        }
      }
      // console.log("After visited: ", visited);
      for (let key of Object.keys(visited)) {
        let [vx, vy] = key.split("_").map(x => parseInt(x));
        holes[keyify([vx, vy])] = insideHole;
        if (insideHole) {
          ret += 1;
        }
      }
    }
  }

  return ret;
};

const dirLengthFromHexColor = (color : string) => {
  console.assert(color.length == 6);

  let length = parseInt(color.substring(0, 5), 16);
  // 0 means R, 1 means D, 2 means L, and 3 means U.
  let dir = {"0": "R", "1": "D", "2": "L", "3": "U"}[color[5]];
  console.log(dir, length);
  return [dir, length];
}

const addSegment = (allSegments, horizontal, start, end) => {
  let cmpI = horizontal ? 0 : 1;
  let otherI = horizontal ? 1 : 0;
  console.assert(start[otherI] == end[cmpI]);
  if (start[cmpI] == end[cmpI]) {
    console.log("1 length item!!! ", horizontal, start, end);
  }

  if (start[cmpI] >= end[cmpI]) {
    [start, end] = [end, start];
  }

  let index = start[otherI];
  let segments = allSegments[index];
  if (segments == null) {
    segments = [];
    allSegments[index] = segments;
  }

  let merged = false;
  for (let i = 0; i < segments.length; i++) {
    let [a, b] = segments[i];
    let aInside = a[cmpI] >= start[cmpI] && a[cmpI] <= end[cmpI];
    let bInside = b[cmpI] >= start[cmpI] && b[cmpI] <= end[cmpI];
    if (aInside || bInside) {
      merged = true;
      let startZ = Math.min(a[cmpI], start[cmpI]);
      let endZ = Math.max(b[cmpI], end[cmpI]);
      if (horizontal) {
        segments[i] = [[startZ, index], [endZ, index]];
      } else {
        segments[i] = [[index, startZ], [index, endZ]];
      }
    }
  }
  if (!merged) {
    segments.push([start, end]);
    segments.sort((a, b) => a[0][cmpI] - b[0][cmpI]);
  }
};

const part2 = (rawInput: string) => {
  let horizontals = {};
  let verticals = {};
  const input = parseInput(rawInput);
  let pos = [0, 0];
  for (let [xDir, xLength, hexColor] of input) {
    let [dir, length] = dirLengthFromHexColor(hexColor);
    let [dx, dy] = DIRS[dir];
    let start = pos;
    let end = [pos[0] + dx * length, pos[1] + dy * length];
    if (dy == 0) {
      addSegment(horizontals, true, start, end);
    } else {
      addSegment(verticals, false, start, end);
    }

    pos = end;
  }

  for (let [key, value] of Object.entries(horizontals)) {
    console.log(key, ":", value);
  }
  for (let [key, value] of Object.entries(verticals)) {
    console.log(key, ":", value);
  }
  //console.log(horizontals, verticals);

  return;
};

run({
  part1: {
    tests: [
{
  input: `R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)`,
  expected: 62,
},
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)`,
  expected: 952408144115,
},
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
