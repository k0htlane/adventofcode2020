def binary_search(fb, code, len):
	if len == 1:
		return 0
	if code[0] == fb[0]:
		return binary_search(fb, code[1:], len//2)
	if code[0] == fb[1]:
		return len//2 + binary_search(fb, code[1:], len//2)

def solve(file):
	ret = 0
	seats = set(range(971)) # I knew from task 1, that the seat numbers run up to 970
	for line in file:
		line.strip()

		# Binary search works well, but I realized while debugging it that
		# using binary numbers gives same thing with even less effort.

		# row = binary_search("FB", line[0:7], 128)
		# col = binary_search("LR", line[7:], 8)

		row = int(line[0:7].replace("F","0").replace("B","1"), base=2)
		col = int(line[7:].replace("L","0").replace("R","1"), base=2)

		ret = max(ret, row*8+col)
		seats.remove(row*8+col)
	print(ret)
	print(seats)

# solve(open("test.txt"))
solve(open("input.txt"))
