import re
import sys

# Tests the line according to Part one
def test_line_1(line: str) -> bool:
    matches = re.match('(\d+)-(\d+) (\w): (.+)', line).groups()
    lower = int(matches[0])
    upper = int(matches[1])
    letter = matches[2]
    password = matches[3]
    num_letters = password.count(letter)
    if num_letters < lower or num_letters > upper:
        return False
    return True

# Tests the line according to Part two
def test_line_2(line: str) -> bool:
    matches = re.match('(\d+)-(\d+) (\w): (.+)', line).groups()
    pos1 = int(matches[0]) - 1
    pos2 = int(matches[1]) - 1
    letter = matches[2]
    password = matches[3]
    pos1_exists = password[pos1] == letter
    pos2_exists = password[pos2] == letter
    if pos1_exists and pos2_exists:
        return False
    if not (pos1_exists or pos2_exists):
        return False
    return True

valid_1 = 0
valid_2 = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if test_line_1(line):
            valid_1 += 1
        if test_line_2(line):
            valid_2 += 1

print(f"Part 1: {valid_1}")
print(f"Part 2: {valid_2}")
