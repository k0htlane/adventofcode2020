def bs(fb, code, len):
	if len == 1:
		return 0
	if code[0] == fb[0]:
		return bs(fb, code[1:], len//2)
	if code[0] == fb[1]:
		return len//2 + bs(fb, code[1:], len//2)

def solve(file):
	ret = 0
	seats = set(range(971))
	for line in file:
		line.strip()
		# row = bs("FB", line[0:7], 128)
		# col = bs("LR", line[7:], 8)
		row = int(line[0:7].replace("F","0").replace("B","1"), base=2)
		col = int(line[7:].replace("L","0").replace("R","1"), base=2)
		# print(row*8+col, row, col)
		ret = max(ret, row*8+col)
		seats.remove(row*8+col)
	print(ret)
	print(seats)

# solve(open("test.txt"))
solve(open("input.txt"))