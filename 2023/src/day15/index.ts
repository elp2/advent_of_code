import run from "aocrunner";

const parseInput = (rawInput: string) => {
  let ret = [];
  let instructions = rawInput.trim().split(",");
  for (let ins of instructions) {
    let name = "";
    let val = null;
    for (let i = 0; i < ins.length; i++) {
      if (ins[i] != "-" && ins[i] != "=") {
        name += ins[i];
      } else {
        if (ins[i] == "=") {
          val = parseInt(ins.substr(i + 1));
        }
        break;
      }
    }

    ret.push([name, hashStr(name), val]);
  }
  return ret;
};

const hashStr = (s: string) => {
  const hashChar = (c: string, ival : number) => {
    // Determine the ASCII code for the current character of the string.
    let ascii = c.charCodeAt(0);
    // Increase the current value by the ASCII code you just determined.
    ival += ascii;
    // Set the current value to itself multiplied by 17.
    ival *= 17;
    // Set the current value to the remainder of dividing itself by 256.
    return ival % 256;
  }

  let ret = 0;
  for (let c of s) {
    ret = hashChar(c, ret);
  }
  return ret;
}

console.assert(hashStr("H") == 200);
console.assert(hashStr("HASH") == 52);

let a = [1,2,3];
console.log(a);
a.splice(1, 1);
console.log(a);

const part1 = (rawInput: string) => {
  const input = rawInput.trim().split(",");
  let ret = 0;
  for (let ins of input) {
    let hashed = hashStr(ins);
    //console.log(ins, " became ", hashed);
    ret += hashed;
  }

  return ret;
};

const focusingPower = (boxes) => {
  let ret = 0;
  for (let boxi = 0; boxi < boxes.length; boxi++) {
    for (let lensi = 0; lensi < boxes[boxi].length; lensi++) {
      // One plus the box number of the lens in question.
      let here = 1 + boxi;
      // The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
      here *= 1 + lensi;
      // The focal length of the lens.      
      here *= boxes[boxi][lensi]["focalLength"];

      ret += here;
    }
  }
  return ret;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  // console.log(input);

  let boxes = [];
  for (let i = 0; i < 256; i++) {
    boxes.push([]);
  }

  for (let [name, boxi, focalLength] of input) {
    let found = false;
    for (let lensi = 0; lensi < boxes[boxi].length; lensi++) {
      let here = boxes[boxi][lensi];
      if (here["name"] == name) {
        found = true;
        if (focalLength == null) {
          boxes[boxi].splice(lensi, 1);
        } else {
          boxes[boxi][lensi]["focalLength"] = focalLength;
        }
        break;
      }
    }
    if (focalLength != null && !found) {
      boxes[boxi].push({"name": name, "focalLength": focalLength});
    }

    // console.log(name, boxi, focalLength, "=> ", boxes[0], boxes[1], boxes[2], boxes[3]);
  }

  return focusingPower(boxes);
};

run({
  part1: {
    tests: [
      {
        input: `rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7`,
        expected: 1320,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7`,
        expected: 145,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
