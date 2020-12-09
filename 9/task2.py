import numpy as np
preamble = []
target = 530627549
# target= 127

sums = [0]
nums = []
for i,line in enumerate(open("input.txt")):
	line = int(line.strip())
	nums.append(line)
	sums.append(sums[-1] + line)
	# assert len(sums) == i+2
	# print("|", nums[-1], sums[-1])
	
	if sums[-1] >= target:
		found = False
		for j in range(i-1, -2, -1):
			if sums[i+1]-sums[j+1] == target:
				found = True
				break
		if found:
			print()
			print(i, j)
			print(nums[j+1:i+1], sum(nums[j+1:i+1]))
			print(sums[i+1],sums[j+1])
			print(np.min(nums[j+1:i+1]))
			print(np.max(nums[j+1:i+1]))
			print(np.max(nums[j+1:i+1])+np.min(nums[j+1:i+1]))
