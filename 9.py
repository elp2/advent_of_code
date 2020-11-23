def remove_garbage(stream):
    ret = ""
    in_garbage = False
    i = 0
    while i < len(stream):
        if stream[i] == "<":
            in_garbage = True
        elif stream[i] == "!":
            assert in_garbage
            i += 1
        elif stream[i] == ">":
            in_garbage = False
        else:
            if not in_garbage:
                ret += stream[i]
        i += 1
    return ret


for garb in ["<>", "<random characters>", "<<<<>", "<{!>}>", "<!!>", "<!!!>>", "<{o\"i!a,<{i<a>"]:
    removed = remove_garbage(garb)
    assert "" == removed

whole_streams = [("{}", 1), ("{{{}}}", 6), ("{{},{}}", 5), ("{{{},{},{{}}}}", 16), ("{<a>,<a>,<a>,<a>}", 1), ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9), ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9), ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)]

def get_score(line, start, base_score):
    score = base_score + 1
    i = start
    while i < len(line):
      if line[i] == "}":
          return (score, i + 1)
      elif line[i] == "{":
          sub_score, i = get_score(line, i + 1, base_score + 1)
          score += sub_score
      else:
          i += 1
    return (score, i)


def get_score_line(line):
    clean = remove_garbage(line)
    print(line, "->", clean)
    score, _ = get_score(clean, 1, 0)
    return score

for ws in whole_streams:
    line, expected = ws
    score = get_score_line(line)
    assert score == expected

print(get_score_line(open("9.txt").readline())) # 14190
