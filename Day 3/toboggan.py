import sys

right = 3
down = 1

trees = 0

x_pos = right
y_pos = down

with open(sys.argv[1], 'r') as f:
    rows = f.readlines()
    print(rows)
    width = len(rows[0]) - 1  # Don't count last newline character
    y_end = len(rows)
    while y_pos < y_end:
        row = rows[y_pos]
        print(f"Hit {row[x_pos % width]} on row {y_pos}, column {x_pos} ({x_pos % width}). Width: {width}")
        print(f"row is {row}")
        if row[x_pos % width] == '#':
            trees += 1
        y_pos += down
        x_pos += right

print(f"Number of trees hit: {trees}")
