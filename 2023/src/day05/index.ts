import run from "aocrunner";
import { parse } from "path";

const parseInput = (rawInput: string) => {
  let seeds = rawInput.split("\n")[0].split(":")[1].trim().split(" ").map(x => parseInt(x.trim()));

  let ret = {"seeds": seeds};

  let tos = rawInput.split("\n\n").slice(1);

  for (let to of tos) {
    let lines = to.split("\n");
    let name = lines[0].split(" ")[0];
    lines = lines.slice(1);
    let ranges = [];
    for (let l of lines) {
      let split = l.split(" ").map(x => parseInt(x.trim()))
      ranges.push(split);
    }
    ret[name] = ranges;
  }

  return ret;
}

const apply_map = (inp, f, t, source) => {
  let key = f + "-to-" + t;
  for (let [dest_start, source_start, length] of inp[key]) {
    if (source >= source_start && source < source_start + length) {
      return source - source_start + dest_start;
    }
  }
  return source;
};


const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  console.log(input);

  let order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"];

  let locations = []
  for (let s of input["seeds"]) {
    for (let i = 0; i < order.length - 1; i++) {
      let f = order[i];
      let t = order[i + 1];
      s = apply_map(input, f, t, s);
    }
    locations.push(s);
  }


  return Math.min(...locations);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

run({
  part1: {
    tests: [
      {
        input: `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`,
        expected: 35,
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
  //onlyTests: true,
});
