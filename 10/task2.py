import numpy as np

data = np.genfromtxt("input.txt", dtype="i")
data.sort()
data = np.concatenate([[0], data, [data[-1]+3]])

diff = data[1:] - data[:-1]

# def count_ways(pos):
# 	if len(next) == 0:
# 		return 1

# 	ret = 0
# 	for i in range(len(next)):
# 		if next[i] - start > 3:
# 			break
# 		# if next[i] - start == 3:
# 			# ret += count_ways(next[i], next[i+1:])
# 		# if next[i] - start == 1:
# 		ret += count_ways(next[i], next[i+1:])

# 	return ret
# print(count_ways(0, data))

count_ways = np.zeros_like(data)
count_ways[-1] = 1
for i in range(1,len(data)+1):
	i = len(data)-i
	for j in range(1,i+1):
		j = i - j
		if data[i]-data[j] > 3:
			break
		count_ways[j] += count_ways[i]
print(count_ways[0])