import numpy as np

data = list(map(lambda l:l.strip(), open("input.txt")))
grid = np.zeros((len(data)+2, 2+len(data[0])), dtype="i1")
for i,line in enumerate(data):
	for j,c in enumerate(line):
		grid[1+i,1+j] = 2 if c == "L" else 0

def update(grid):
	ret = np.zeros_like(grid)
	updates = 0
	for i in range(1,ret.shape[0]-1):
		for j in range(1,ret.shape[1]-1):
			# if i==1 and j==1:
				# print(grid[i-1:i+2,j-1:j+2])
			if grid[i,j] == 2 and np.sum(grid[i-1:i+2,j-1:j+2] & 1) == 0:
				ret[i,j] = 3
				updates += 1
			elif grid[i,j] == 3 and np.sum(grid[i-1:i+2,j-1:j+2] & 1) >= 5:
				ret[i,j] = 2
				updates += 1
			else:
				ret[i,j] = grid[i,j]
	return updates, ret

print(grid)
n = 0
while True:
	updates, grid = update(grid)
	# print(grid)
	if updates == 0:
		print(np.sum(grid&1))
		break
	n += 1
	assert n < 100

