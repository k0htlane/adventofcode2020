import numba
import sys
import numpy as np

def parse(line):
	ret = []
	while len(line) > 0:
		if line.startswith("e"):
			ret.append((1,0))
			line = line[1:]
		elif line.startswith("w"):
			ret.append((-1,0))
			line = line[1:]
		elif line.startswith("sw"):
			ret.append((-0.5,-0.5))
			line = line[2:]
		elif line.startswith("se"):
			ret.append((0.5,-0.5))
			line = line[2:]
		elif line.startswith("nw"):
			ret.append((-0.5,0.5))
			line = line[2:]
		elif line.startswith("ne"):
			ret.append((0.5,0.5))
			line = line[2:]
	return ret


class Grid:
	def __init__(self):
		self.data = set()
		self.lb = 0, 0
		self.ub = 0, 0

	def __getitem__(self, index):
		return index in self.data
	
	def __setitem__(self, index, value):
		if not value and index in self.data:
			self.data.remove(index)
		elif value:
			self.data.add(index)
		
		self.lb = min(self.lb[0], index[0]), min(self.lb[1], np.floor(index[1]))
		self.ub = max(self.ub[0], index[0]), max(self.ub[1], index[1])
	
	def asarray(self):
		size = np.array(self.ub) - np.array(self.lb)
		size = size.astype(np.int)
		ret = np.zeros((size[0]+1, 2+size[1]*2), dtype=np.int8)
		for x,y in sorted(self.data):
			x, y = x-self.lb[0], y-self.lb[1]
			ret[int(x), int(2*y)] = 1
			# print(f"({x}, {y}) ==> ({int(x)}, {int(2*y)})")
		return ret

grid = Grid()

for line in sys.stdin:
	line = line.strip()
	pos = (0, 0.)
	for dx,dy in parse(line):
		pos = pos[0]+dx, pos[1]+dy
	grid[pos[0], pos[1]] = not grid[pos[0], pos[1]]


# # for x,y in sorted(grid.data):
for x,y in [(0, 0)]:
	# x, y = x+grid.lb[0], y+grid.lb[1]
	nbors = 0
	for dx, dy in [(-1, 0), (1, 0), (-0.5, -0.5), (0.5,-0.5), (-0.5, 0.5), (0.5, 0.5)]:
		if grid[x+dx,y+dy]:
			nbors += 1
		# 	print(f"[*] ({x+dx-grid.lb[0]:+.1f}, {y+dy-grid.lb[1]:+.1f}) [{int(x+dx-grid.lb[0])}, {int(2*(y+dy-grid.lb[1]))}]")
		# else:
		# 	print(f"[.] ({x+dx-grid.lb[0]:+.1f}, {y+dy-grid.lb[1]:+.1f}) [{int(x+dx-grid.lb[0])}, {int(2*(y+dy-grid.lb[1]))}]")
	print(f"({x-grid.lb[0]}, {y-grid.lb[1]}) = {nbors} [{int(x-grid.lb[0])}, {int(2*(y-grid.lb[1]))}]")
print()

grid = grid.asarray()

@numba.jit
def step(grid):
	grid = np.pad(grid, 2)
	padded = np.pad(grid, 1)
	# for i,j in np.ndindex(grid.shape):
	for i in range(1,grid.shape[0]+1):
		for j in range(1,grid.shape[1]+1):
			# i, j = i+1, j+1
			nbors = padded[i-1,j] + padded[i+1,j]
			if j%2 == 1:
				nbors += padded[i, j+1] + padded[i-1, j+1]
				nbors += padded[i, j-1] + padded[i-1, j-1]
			else:
				nbors += padded[i, j+1] + padded[i+1, j+1]
				nbors += padded[i, j-1] + padded[i+1, j-1]

			if padded[i,j] == 1 and (nbors == 0 or nbors > 2):
				grid[i-1,j-1] = 0
			elif padded[i,j] == 0 and nbors == 2:
				grid[i-1,j-1] = 1
	return grid

print(0, np.sum(grid))
for i in range(100):
	grid = step(grid)
	if (1+i) % 10 == 0:
		print(1+i, np.sum(grid))
	