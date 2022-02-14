import re

with open("map-of-the-tunnels.txt", "r") as f:
    map = f.readlines()
with open("list-of-instructions.txt", "r") as f:
    ins = f.readlines()
x, y = 3, 21
for item in ins:
    for step in re.split("[^A-Z]", item):
        backup_x, backup_y = x, y
        if step == "E":
            x += 1
        elif step == "W":
            x -= 1
        elif step == "S":
            y += 1
        elif step == "N":
            y -= 1
        if map[y][x] == "█":
            x, y = backup_x, backup_y
print(x, y)
