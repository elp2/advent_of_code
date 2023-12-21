import run from "aocrunner";
import { timeStamp } from "console";

const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let times = lines[0].split(":")[1].split(" ").map(x => parseInt(x.trim()));
  times = times.filter(t=> !Number.isNaN(t));
  let distances = lines[1].split(":")[1].split(" ").map(x => parseInt((x.trim())));
  distances = distances.filter(t=> !Number.isNaN(t));

  return {"times": times, "distances": distances};
};

const parseInput2 = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let time = parseInt(lines[0].split(":")[1].replace(/\s/g, ""));
  let distance = parseInt(lines[1].split(":")[1].replace(/\s/g, ""));

  return {"time": time, "distance": distance};
};

function bisect(f: (x: number) => boolean, low: number, high: number): number | null {
  while (low < high) {
    let mid = Math.floor(low + (high - low) / 2);
    if (f(mid)) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }

  if (low === high && f(low)) {
    return low;
  }

  return null; // Indicate no change in behavior was found in the range
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  console.log(input);
  
  let ret = 1;

  for (let i = 0; i < input.times.length; i++) {
    let t = input.times[i];
    let d = input.distances[i];

    let hlow = 1;
    for (hlow = 1; hlow < t - 1; hlow++) {
      if (hlow * (t - hlow) > d) {
        break;
      }
    }
    let hhigh = t - 1;
    for (hhigh = t - 1; hhigh > hlow; hhigh--) {
      if (hhigh * (t - hhigh) > d) {
        break;
      }
    }
    let margin = hhigh - hlow + 1;
    console.log(margin, hlow, hhigh);
    ret *= margin;
  }

  return ret;
};

const part2 = (rawInput: string) => {
  const input = parseInput2(rawInput);
  console.log(input);
  let t = input.time;
  let d = input.distance;

  let makesIt = (holdTime: number) => {
    return (input.time - holdTime) * holdTime > input.distance;
  };

  let low = bisect(makesIt, 1, input.time);
  console.log("low: ", low);
  let high = bisect((x: number) => {return !makesIt(x)}, low + 1, input.time);
  console.log(high);

  return high - low;
};

run({
  part1: {
    tests: [
      {
        input: `Time:      7  15   30
Distance:  9  40  200`,
        expected: 288,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `Time:      71530
Distance:  940200`,
        expected: 71503,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
