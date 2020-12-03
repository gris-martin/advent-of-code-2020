import sys
from typing import List

def test_slope(rows: List[str], right: int, down: int) -> int:
    x = right
    y = down
    trees = 0
    width = len(rows[0].strip())
    height = len(rows)
    while y < height:
        row = rows[y]
        if row[x % width] == '#':
            trees += 1
        y += down
        x += right
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
