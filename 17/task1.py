import numpy as np

def step(cubes):
	ret = np.zeros_like(cubes)
	N, _, M = ret.shape
	for i in range(1, N-1):
		for j in range(1, N-1):
			for k in range(1, M-1):
				s = np.sum(cubes[i-1:i+2, j-1:j+2, k-1:k+2]) - cubes[i,j,k]
				if cubes[i,j,k]==1 and (s == 2 or s == 3):
					ret[i,j,k] = 1
				elif cubes[i,j,k]==0 and s==3:
					ret[i,j,k] = 1
	return ret

data = list(map(lambda l: list(l.strip()), open("/dev/stdin")))
data = np.array(data)
print(data)
pad=10
N = len(data) + 2*pad
cubes = np.zeros((N, N, 2*pad), dtype="u1")

for (i,j), c in np.ndenumerate(data):
	if c == "#":
		cubes[pad+i, pad+j, pad] = 1

for i in range(6):
	cubes = step(cubes)
print(np.sum(cubes))
assert np.sum(cubes) > 345