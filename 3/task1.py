col = 0
ret = 0
for line in open("input.txt", "r"):
	line = line.strip()
	if line[col%len(line)] == "#":
		ret += 1
	col += 3
print(ret)
