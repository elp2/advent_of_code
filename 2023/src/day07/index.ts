import run from "aocrunner";

let FIVE_OF_A_KIND=100; //
let FOUR_OF_A_KIND=99; // 
let FULL_HOUSE=98
let THREE_OF_A_KIND=97; //
let TWO_PAIR=96; //
let ONE_PAIR=95; //
let HIGH_CARD=94; 

function arrEq(arr1: number[], arr2: number[]) {
  if (arr1.length != arr2.length) {
    return false;
  }
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] != arr2[i]) {
      return false;
    }
  }
  return true;
}

function parseCard(card: string) {
  if (card == "T") {
    return "10";
  } else if (card == "J") {
    return "11";
  } else if (card == "Q") {
    return "12";
  } else if (card == "K") {
    return "13";
  } else if (card == "A") {
    return "14";
  }
  return card;
}

function handDict(cards: string) {
  let cdict = {};
  for (let c of cards) {
    c = parseCard(c);
    if (c in cdict) {
      cdict[c] += 1;
    } else {
      cdict[c] = 1;
    }
  }
  return cdict;
}

const handType = (cards: string) => {
  let cdict = handDict(cards);

  let values = Object.values(cdict).sort();
  if (values.length == 1) {
    return FIVE_OF_A_KIND;
  } else if (arrEq(values, [1, 4])) {
      return FOUR_OF_A_KIND;
  } else if (arrEq(values, [2, 3])) {
    return FULL_HOUSE;
  } else if (arrEq(values, [1, 1, 3])) {
    return THREE_OF_A_KIND;
  } else if (arrEq(values, [1, 2, 2])) {
    return TWO_PAIR;
  } else if (arrEq(values, [1, 1, 1, 2])) {
    return ONE_PAIR;
  } else if (arrEq(values, [1, 1, 1, 1, 1])) {
    return HIGH_CARD;
  }
  console.log("shouldn't happen");
  return null;
}

function winner(a, b) {
  if (a.storedType != b.storedType) {
    return a.storedType - b.storedType;
  }

  for (let i = 0; i < 5; i++) {
    let ac = parseInt(parseCard(a.cards[i]));
    let bc = parseInt(parseCard(b.cards[i]));
    if (ac > bc) {
      return 1;
    } else if (bc > ac) {
      return -1;
    }
    console.log(i, ac, bc);
  }

  console.log("shouldn't happen!!!", a, b);
  return 0;
}


const parseInput = (rawInput: string) => {
  let lines = rawInput.split("\n");
  let ret = [];
  for (let l of lines) {
    // console.log(l);
    let hand = {};
    hand["cards"] = l.split(" ")[0];
    hand["bid"] = parseInt(l.split(" ")[1]);
    hand["storedType"] = handType(hand["cards"]);
    ret.push(hand);
  }
  return ret;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  console.log(input);
  input.sort(winner);
  console.log(input);

  let wins = 0;
  for (let i = 0; i < input.length; i++) {
    wins += (i + 1) * input[i].bid;
  }

  return wins;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

run({
  part1: {
    tests: [
      {
        input: `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483`,
        expected: 6440,
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
