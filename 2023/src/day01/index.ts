import run from "aocrunner";

let NUMBERS="0123456789";

let NUMBERS2={"one": "1", 
"two": "2",
"three": "3",
"four": "4",
"five": "5",
"six": "6",
"seven": "7",
"eight": "8",
"nine": "9",
"0": "0",
"1": "1",
"2": "2",
"3": "3",
"4": "4",
"5": "5",
"6": "6",
"7": "7",
"8": "8",
"9": "9",

};

const parseInput1 = (rawInput: string) => {
  const lines = rawInput.split("\n");
  var nums = [];
  for (let line of lines) {
    var lineNums = []
    for (let char of line) {
      if (NUMBERS.includes(char)) {
        lineNums.push(char);
      }
    }
    nums.push(lineNums);
  }

  return nums
}
const parseInput2 = (rawInput: string) => {
  const lines = rawInput.split("\n");
  var nums = [];
  for (let line of lines) {
    var lineNums = []
    for (let i = 0; i < line.length; i++) {
      for (let [name, num] of Object.entries(NUMBERS2)) {
        let str = line.substring(i, i + name.length);
        if (str == name) {
          lineNums.push(num);
        }
      }
    }
    nums.push(lineNums);
  }

  return nums
}

const part1 = (rawInput: string) => {
  const nums = parseInput1(rawInput);

  let ret = 0;
  for (let num of nums) {
    let first = num[0];
    let last = num[num.length - 1];
    let here = first + last;
    ret += parseInt(here);
  }
  
  return ret;
};

const part2 = (rawInput: string) => {
  const input = parseInput2(rawInput);

  let ret = 0;
  for (let num of input) {
    let first = num[0];
    let last = num[num.length - 1];
    let here = first + last;
    ret += parseInt(here);
  }
  

  return ret;
};

run({
  part1: {
    tests: [
      {
        input: `1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet`,
        expected: 142,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen`,
        expected: 281,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
