import run from "aocrunner";
import { ServerResponse } from "http";

const parseInput = (rawInput: string) => {
  let rulesDir = {}; 
  let [rulesLines, partsLines ] = rawInput.split("\n\n");

  for (let l of rulesLines.split("\n")) {
    let [name, rawRules] = l.split("{");
    // console.log(name, rawRules);
    rawRules = rawRules.substring(0, rawRules.length - 1);
    let rules = [];
    for (let rawRule of rawRules.split(",")) {
      let condition = null;
      if (rawRule.length == 1 || rawRule.indexOf(":") == -1) {
        rules.push({"condition": null, "dest": rawRule});
      } else {
        let key = rawRule[0];
        let condition = rawRule[1];
        let val = parseInt(rawRule.substring(2));
        let dest = rawRule.split(":")[1];
        rules.push({"condition": condition, "key": key, "val": val, "dest": dest});
      }
    }
    rulesDir[name] = rules;
  }

  let parts = [];
  for (let l of partsLines.split("\n")) {
    l = l.substring(1, l.length - 1);
    let part = {};
    for (let kv of l.split(",")) {
      let [k, v] = kv.split("=");
      part[k] = parseInt(v);
    }
    parts.push(part);
  }

  return [rulesDir, parts];
};

const partAccepted = (allRules, part) => {
  // console.log(part);
  let state = "in";
  while (true) {
    // console.log(state);
    if (state == "A") {
      return true;
    } else if (state == "R") {
      return false;
    }

    let stateRules = allRules[state];
    for (let rule of stateRules) {
      let condition = rule["condition"];
      let key = rule["key"];
      let val = rule["val"];
      let dest = rule["dest"];
      if (condition == null) {
        state = rule["dest"];
        break;
      } else if (condition == ">") {
        if (part[key] > val) {
          state = rule["dest"];
          break;
        }
      } else if (condition == "<") {
        if (part[key] < val) {
          state = rule["dest"];
          break;
        }
      }
      // console.log(rule, state);
    }
  }
}

const part1 = (rawInput: string) => {
  const [rules, parts] = parseInput(rawInput);

  let ret = 0;

  for (let i = 0; i < parts.length; i++) {
    let part = parts[i];
    if (partAccepted(rules, part)) {
      let here = 0;
      for (let k of ["x", "m", "a", "s"]) {
        here += part[k];
      }
      ret += here;
    }
  }


  return ret;
};

function deepCopyDictWithArrayValues<T>(dict: Record<string, T[]>): Record<string, T[]> {
  const newDict: Record<string, T[]> = {};

  for (const key in dict) {
      if (dict.hasOwnProperty(key)) {
          // Assuming T is a primitive type. For complex types, a deeper copy logic is needed.
          newDict[key] = [...dict[key]];
      }
  }

  return newDict;
}

const part2 = (rawInput: string) => {
  const [rules, parts] = parseInput(rawInput);

  // Start with all possibilities.
  let inRanges = {"x": [0, 4000], "m": [0, 4000], "a": [0, 4000], "s": [0, 4000]};

  let stateRanges = {};
  let queue = [["in", inRanges]];

  const maybeQueuePush = (state, partRange) => {
    let valid = true;
    for (let char of "xmas") {
      if (partRange[char][0] > partRange[char][1]) {
        valid = false;
      }
    }
    if (valid) {
      queue.push([state, partRange]);
    } else {
      console.log("Not valid: ", partRange);
    }
  };

  const applyRule = (rule, partRange) => {
    let remainder = {...partRange};

    let condition = rule["condition"];
    let key = rule["key"];
    let val = rule["val"];
    let dest = rule["dest"];
    if (condition == null) {
      return [dest, remainder, null];
    } else if (condition == ">") {
      let matching = deepCopyDictWithArrayValues(remainder);
      matching[key][0] = val + 1;
      remainder[key][1] = val;
      return [dest, matching, remainder];
    } else if (condition == "<") {
      let matching = deepCopyDictWithArrayValues(remainder);
      matching[key][1] = val - 1;
      remainder[key][0] = val;
      console.log(matching, remainder);
      return [dest, matching, remainder];
    }
    console.assert(false); blowup;
  };

  while (queue.length > 0) {
    let [state, partRanges] = queue.shift();
    let sr = stateRanges[state];
    if (sr == null) {
      sr = [];
      stateRanges[state] = sr;
    }
    sr.push(partRanges);
    console.log(partRanges);

    let remainder = partRanges;
    if (rules[state] == null) {
      console.log("NO RULES FOR: ", state);
      continue;
    }
    for (let rule of rules[state]) {
      let [newState, applied, notApplied] = applyRule(rule, remainder);
      maybeQueuePush(newState, applied);
      remainder = notApplied;
    }
  }

  console.log("---------\n", stateRanges, "--------\n");

  console.log("A", stateRanges["A"]);
  // let ret = 1;
  // for (let char of "xmas") {
  //   let here = 0;
  //   for (let [start, end] of stateRanges["in"][char]) {
  //     here += (end - start) + 1;
  //   }
  //   ret *= here;
  // }
  return -123;
  return ret;
};

run({
  part1: {
    tests: [
      {
        input: `px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}`,
        expected: 19114,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}`,
        expected: 167409079868000,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
