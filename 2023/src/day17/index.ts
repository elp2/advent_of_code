import run from "aocrunner";

let DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]];
const turnLeft = (dir: number) => {
  return (dir + 4 - 1) % 4;
}

const turnRight = (dir: number) => {
  return (dir + 1) % 4;
}

const moveDir = (dir: number, x: number, y: number) => {
  return [x + DIRS[dir][0], y + DIRS[dir][1]];
};

const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let ret = [];
  for (let l of lines) {
    ret.push(l.split("").map(x => parseInt(x)));
  }
  return ret;
};

const keyify = (x, y, dir, straightLength) => {
  return `${x}_${y}_${dir}_${straightLength}`;
};

const shouldPush = (seen, x, y, dir, straightLength, heatLoss) => {
  return true;
  // It seems like we should be able to ignore any incoming paths that have a similar / worse heatloss, going the same direction, with higher straightLengths?
  for (let os = straightLength - 1; os >= 0; os--) {
    let otherHeatLoss = seen[keyify(x, y, dir, os)];
    if (otherHeatLoss != null && heatLoss >= otherHeatLoss) {
      // Can get here with same heatloss and less straight
      return false;
    }
  }
  return true;
}

const traverse = (board) => {
  let minHeatLoss = 10000000000;
  let onBoard = (x, y) => {
    return (y >= 0 && y < board.length && x >=0 && x < board[y].length);
  };

  let seen = {};
  let queue = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 0]];

  let queuePush = (x, y, dir, newStraightLength, heatLoss) => {
    let [nx, ny] = moveDir(dir, x, y);
    if (!onBoard(nx, ny)) {
      return;
    }
    let newHeatLoss = heatLoss + board[ny][nx];
    if (shouldPush(seen, x, y, dir, newStraightLength, newHeatLoss)) {
      queue.push([nx, ny, dir, newStraightLength, newHeatLoss]);
    }
  };

  let atEnd = (x, y) => {
    return (x == board[0].length - 1 && y == board.length - 1);
  };

  //let stop = 0;
  let step = 0;
  console.log("board = ", board[0].length, " x ", board.length);
  while (queue.length > 0) {
    step += 1;
    let [x, y, dir, straightLength, heatLoss] = queue.shift();
    if (step % 10000 == 0) {
      console.log(x, y, dir, straightLength, heatLoss, queue.length, Object.keys(seen).length);
    }
    let seenKey = keyify(x, y, dir, straightLength);
    let prevHeatLoss = seen[seenKey];
    if (prevHeatLoss != null && heatLoss >= prevHeatLoss) {
      continue;
    }
    for (let os = straightLength; os < 3; os++) {
      seen[keyify(x, y, dir, os)] = heatLoss;
    }
    if (atEnd(x, y)) {
      minHeatLoss = Math.min(heatLoss, minHeatLoss);
      continue;
    }


    queuePush(x, y, turnLeft(dir), 0, heatLoss);    
    queuePush(x, y, turnRight(dir), 0, heatLoss);
    if (straightLength < 2) {
      queuePush(x, y, dir, straightLength + 1, heatLoss);
    }
  }

  return minHeatLoss;
};

const part1 = (rawInput: string) => {
  const board = parseInput(rawInput);

  return traverse(board);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

run({
  part1: {
    tests: [
{
input: `2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533`,
expected: 102,
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
