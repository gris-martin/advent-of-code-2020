import sys
from typing import List

def test_slope(rows: List[str], right: int, down: int) -> int:
    x_pos = right
    y_pos = down
    trees = 0
    width = len(rows[0].strip())
    y_end = len(rows)
    while y_pos < y_end:
        row = rows[y_pos]
        if row[x_pos % width] == '#':
            trees += 1
        y_pos += down
        x_pos += right
    return trees

with open(sys.argv[1], 'r') as f:
    rows = f.readlines()

    # Part 1
    print(f"Part 1: {test_slope(rows, 3, 1)}")

    # Part 2
    trees = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees *= test_slope(rows, *slope)
    print(f"Part 2: {trees}")
