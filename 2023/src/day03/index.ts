import run from "aocrunner";

let NUMBERS="0123456789";
let EMPTY=".";


const at = (grid: Array<string>, x: number, y : number) => {
  if (y >= grid.length || y < 0) {
    return EMPTY;
  }
  if (x >= grid[y].length || x < 0) {
    return EMPTY;
  }
  return grid[y][x];
}

const parseInput = (rawInput: string) => {
  let grid = [];
  for (let line of rawInput.split("\n")) {
    line = line.trim();
    grid.push(line);
  }

  let ret = {};
  for (let y = 0; y < grid.length; y++) {
    let line = grid[y];
    for (let x = 0; x < line.length; x++) {
      let c = line[x];
      if (!NUMBERS.includes(c)) {
        continue;
      }

      let name = "";
      let symbol = EMPTY;
      while (x < line.length) {
        c = line[x];
        if (!NUMBERS.includes(c)) {
          break;
        }
        name += c;

        for (let dx = x - 1; dx < x + 2; dx++) {
          for (let dy = y - 1; dy < y + 2; dy++) {
            let a = at(grid, dx, dy);
            if (!NUMBERS.includes(a) && a != EMPTY) {
              symbol = a;
            }
          }
        }

        x += 1;
      }
      if (symbol != EMPTY) {
        if (name in ret) {
          ret[name].push(symbol);
        } else {
          ret[name] = [symbol];
        }
//        ret[name] = symbol;

      }
    }
  }

  // console.log(ret);
  return ret;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  let ret = 0;
  for (let [num, parts] of Object.entries(input)) {
    for (let parttype of parts) {
      ret += parseInt(num); // parttype;
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
        input: `467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..`,
        expected: 4361,
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
