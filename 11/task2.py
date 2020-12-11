import numpy as np

data = list(map(lambda l:l.strip(), open("input.txt")))
grid = np.zeros((len(data)+2, 2+len(data[0])), dtype="i1")
for i,line in enumerate(data):
	for j,c in enumerate(line):
		grid[1+i,1+j] = 2 if c == "L" else 0

def viscount(grid, i0, j0):
	N,M = grid.shape
	dirv = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
	mask = [1]*8
	nbor = [0]*8
	m = 0
	while sum(mask) > 0:
		m += 1
		for n,v in enumerate(dirv):
			if mask[n]==0:
				continue
			i = v[0]*m+i0
			j = v[1]*m+j0
			if i <= 0 or j <= 0 or i >= N-1 or j >= M-1:
				mask[n] = 0
				continue
			if grid[i,j]&2 == 2:
				nbor[n] = grid[i,j]&1
				mask[n] = 0
	return sum(nbor)



def update(grid):
	ret = np.zeros_like(grid)
	updates = 0
	for i in range(1,ret.shape[0]-1):
		for j in range(1,ret.shape[1]-1):
			if grid[i,j] == 2 and viscount(grid,i,j) == 0:
				ret[i,j] = 3
				updates += 1
			elif grid[i,j] == 3 and viscount(grid,i,j) >= 5:
				ret[i,j] = 2
				updates += 1
			else:
				ret[i,j] = grid[i,j]
	return updates, ret

# print(grid)
n = 0
while True:
	updates, grid = update(grid)
	# print(grid)
	if updates == 0:
		print(">>", np.sum(grid&1))
		break
	n += 1
	print(n, f"updates={updates}")
	# assert n < 1000

