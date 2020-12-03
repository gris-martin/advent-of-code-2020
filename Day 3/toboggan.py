import sys

right = 3
down = 1

trees = 0

x_pos = right
y_pos = down

with open(sys.argv[1], 'r') as f:
    rows = f.readlines()
    width = len(rows[0]) - 1  # Don't count last newline character
    y_end = len(rows)
    while y_pos < y_end:
        row = rows[y_pos]
        if row[x_pos % width] == '#':
            trees += 1
        y_pos += down
        x_pos += right

print(f"Number of trees hit: {trees}")
