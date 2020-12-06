import numpy as np

def slope(right, down):
	col = 0
	ret = 0
	for i,line in enumerate(open("input.txt", "r")):
		if down > 1 and i%down != 0:
			continue
		line = line.strip()
		if line[col%len(line)] == "#":
			ret += 1
		col += right
	return ret

sol = []
sol.append(slope(1, 1))
sol.append(slope(3, 1))
sol.append(slope(5, 1))
sol.append(slope(7, 1))
sol.append(slope(1, 2))
print(np.prod(sol))