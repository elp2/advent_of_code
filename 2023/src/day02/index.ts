import run from "aocrunner";

const parseInput = (rawInput: string) => {
  let ret = {}
  for (let line of rawInput.split("\n")) {
    line = line.trim();
    // console.log(line);
    let game = line.split(":");
    let gamenum = game[0].split(" ")[1];
    // for (let g of game[1]) {
    let gret = []
    for (let draws of game[1].split(";")) {
      let dret = {}
      for (let draw of draws.split(",")) {
        draw = draw.trim();
        let [num, color] = draw.split(" ");
        dret[color] = parseInt(num);
      }
      gret.push(dret);
    }

    ret[gamenum] = gret;
    // }
  }
  // console.log(ret);
  return ret;
};

const valid1 = (game, cubes) => {
  for (let draw of game) {
    for (let [color, colorNum] of Object.entries(draw)) {
      if (!(color in cubes) || cubes[color] < colorNum) {
        return false;
      }
    }
  }

  return true;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  // console.log(input);
  let cubes = {"red": 12, "green": 13, "blue": 14};
  let ret = 0;
  for (let [gameId, game] of Object.entries(input)) {

    if (valid1(game, cubes)) {
      ret += parseInt(gameId);
    }
  }

  return ret; // 2560 too low
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let ret = 0;

  for (let [gameId, game] of Object.entries(input)) {
    let mins = {"red": 0, "green": 0, "blue": 0};
    for (let draw of game) {
      for (let [color, colorNum] of Object.entries(draw)) {
        if (colorNum > mins[color]) {
          mins[color] = colorNum;
        }
      }
    }
    ret += mins["red"] * mins["green"] * mins["blue"];
  }
  return ret;
};

run({
  part1: {
    tests: [
      {
        input: `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`,
        expected: 8,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`,
        expected: 2286,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
