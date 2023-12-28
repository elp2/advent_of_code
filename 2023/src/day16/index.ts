import run from "aocrunner";

const parseInput = (rawInput: string) => {
  return rawInput.split("\n");
};

const energizedDirections = (board, queueStart) => {
  let ed = {};
  let edKey = (x, y, dx, dy) => {
    return x + "_" + y + "_" + dx + "_" + dy;
  };
  // console.log(board);
  let queue = [queueStart];
  while (queue.length > 0) {
    let [x, y, dx, dy] = queue.shift();
    if (x < 0 || y < 0 || y >= board.length || x >= board[y].length ) {
      continue;
    }
    let key = edKey(x, y, dx, dy);
    if (key in ed) {
      continue;
    }

    ed[key] = true;
    let here = board[y][x];

    // console.log(here, [x, y, dx, dy]);
    let qp = (x, y, dx, dy) => {
      let enq = [x + dx, y + dy, dx, dy];
      //console.log("Adding: ", enq);
      queue.push(enq);
    }
    // .), mirrors (/ and \), and splitters (| and -
    if ("." == here) {
      qp(x, y, dx, dy);
    } else if ("|" == here) {
      if (dx != 0) {
        // only split on horiz.
        qp(x, y, 0, 1);
        qp(x, y, 0, -1);
      } else {
        qp(x, y, dx, dy);
      }
    } else if ("-" == here) {
      if (dy != 0) {
        // only split vert.
        qp(x, y, -1, 0);
        qp(x, y, 1, 0);
      } else {
        qp(x, y, dx, dy);
      }
    } else if ("/" == here) {
      if (dx == 1) {
        qp(x, y, 0, -1);
      } else if (dx == -1) {
        qp(x, y, 0, 1);
      } else if (dy == 1) {
        qp(x, y, -1, 0);
      } else if (dy == -1) {
        qp(x, y, 1, 0);
      } else {
        console.log("unexpeced: /[", here, "]")
        console.assert(false);
  
      }
    } else if ("\\" == here) {
      if (dx == 1) {
        qp(x, y, 0, 1);
      } else if (dx == -1) {
        qp(x, y, 0, -1);
      } else if (dy == 1) {
        qp(x, y, 1, 0);
      } else if (dy == -1) {
        qp(x, y, -1, 0);
      } else {
        console.log("unexpeced: \\[", here, "]")
        console.assert(false);
  
      }
    } else {
      console.log("unexpeced: [", here, "]")
      console.assert(false);
    }
    // console.log("Queue now: ", queue);
  }


  let ret = {};
  for (let k of Object.keys(ed)) {
    let [x, y, dx, dy] = k.split("_").map(x => parseInt(x));
    ret[x + "_" + y] = true;
  }

  return Object.keys(ret).length;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return energizedDirections(input, [0, 0, 1, 0]);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  let ret = 0;
  for (let x = 0; x < input[0].length; x++) {
    ret = Math.max(ret, energizedDirections(input, [x, 0, 0, 1]));
    ret = Math.max(ret, energizedDirections(input, [x, input.length - 1, 0, -1]));
  }

  for (let y = 0; y < input.length; y++) {
    ret = Math.max(ret, energizedDirections(input, [0, y, 1, 0]));
    ret = Math.max(ret, energizedDirections(input, [input[0].length - 1, y,-1, 0]));
  }

  return ret;
};

run({
  part1: {
    tests: [
  {
    input: `.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....`,
expected: 46,
  },
    ],
    solution: part1,
  },
  part2: {
    tests: [
{
    input: `.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....`,
expected: 51,
  },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
