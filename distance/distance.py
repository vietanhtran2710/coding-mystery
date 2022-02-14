import enum


with open("2d-grid-of-particles.txt", "r") as f:
    grid = f.readlines()
result = 0
for x_ind, row in enumerate(grid):
    for y_ind, cell in enumerate(row):
        if cell == '•':
            result += abs(x_ind - 26) + abs(y_ind - 51)
print(result)
