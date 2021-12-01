# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# input is 382345-843167.

input_from = 382345
input_to = 843167

# 382345-843167
def is_valid_password(password):
    s = str(password)
    has_doubled = s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4] or s[4] == s[5]
    increases = int(s[0]) <= int(s[1]) and int(s[1]) <= int(s[2]) and int(s[2]) <= int(s[3]) and int(s[3]) <= int(s[4]) and int(s[4]) <= int(s[5])
    return has_doubled and increases

# print(is_valid_password(111111))
# print(is_valid_password(223450))
# print(is_valid_password(123789))
print(is_valid_password(678900))

num_passwords = 0
for password in range(input_from, input_to):
    if is_valid_password(password):
        # print(password)
        num_passwords += 1

print(num_passwords)