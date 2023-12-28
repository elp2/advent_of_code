import run from "aocrunner";

const parseInput = (rawInput: string) => {
  return rawInput.split("\n");
};

const energizedDirections = (board) => {
  let queue = [[0, 0, 1, 0]];
  let ed = {};
  let edKey = (x, y, dx, dy) => {
    return x + "_" + y + "_" + dx + "_" + dy;
  };
  // console.log(board);
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

  return ed;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  let energized = {};
  let ed = energizedDirections(input);
  // console.log(ed);
  for (let k of Object.keys(ed)) {
    let [x, y, dx, dy] = k.split("_").map(x => parseInt(x));
    energized[x + "_" + y] = true;
  }

  return Object.keys(energized).length;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
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
