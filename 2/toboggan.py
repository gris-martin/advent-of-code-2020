import re
import sys

def test_line(line: str) -> bool:
    matches = re.match('(\d+)-(\d+) (\w): (.+)', line).groups()
    lower = int(matches[0])
    upper = int(matches[1])
    letter = matches[2]
    password = matches[3]
    num_letters = password.count(letter)
    if num_letters < lower or num_letters > upper:
        return False
    return True

corrupted = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if test_line(line):
            corrupted += 1

print(corrupted)
