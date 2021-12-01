def count_valid_passphrases():
    valid = 0
    for phrase in open('4.txt').readlines():
        invalid = False
        words = phrase.split(' ')
        seen = {}
        for word in words:
            word = word.strip()
            print('[%s]' % word)
            if word in seen:
                invalid = True
            seen[word] = True
        if not invalid:
            valid += 1
    print(valid)

# scount_valid_passphrases() # 477

from collections import defaultdict

def ret_zero():
    return 0

def count_valid_passphrases2():
    valid = 0
    for phrase in open('4.txt').readlines():
        invalid = False
        words = phrase.split(' ')
        seen = {}
        for word in words:
            word = word.strip()
            chars = list(word)
            chars.sort()
            word_chars = ''.join(chars)
            if word_chars in seen:
                invalid = True
            seen[word_chars] = True

        if not invalid:
            valid += 1
    print(valid)

count_valid_passphrases2() # 167
