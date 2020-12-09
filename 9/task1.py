preamble = []
PRE = 25
for i,line in enumerate(open("input.txt")):
	line = int(line.strip())
	if i < PRE:
		preamble.append(int(line))
		continue
	sums = set()
	for a_i, a in enumerate(preamble):
		for b_i, b in enumerate(preamble):
			if a_i != b_i:
				sums.add(a+b)

	if line not in sums:
		print(line)
		exit(0)
	
	preamble.pop(0)
	preamble.append(line)



