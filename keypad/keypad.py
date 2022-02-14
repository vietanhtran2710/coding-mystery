with open("blank-sheet-of-paper.txt", "r") as f:
    blank_sheet_lines = f.readlines()
with open("shredded-sheet-of-paper.txt", "r") as f:
    shredded = f.readlines()
result = []
for line in blank_sheet_lines:
    brand = line[:20]
    for shredded_line in shredded:
        if shredded_line.startswith(brand):
            result.append(shredded_line)
            shredded.remove(shredded_line)
with open("result.txt", "w") as f:
    f.writelines(result)