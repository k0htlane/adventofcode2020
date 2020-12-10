import numpy as np

data = np.genfromtxt("test.txt", dtype="i")
data.sort()
data = np.concatenate([[0], data, [data[-1]+3]])

diff = data[1:] - data[:-1]
print(diff)

print(np.count_nonzero(diff==3)*np.count_nonzero(diff==1))