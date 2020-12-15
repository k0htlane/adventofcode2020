import itertools

nrs = list(map(int,input().split(",")))

spoken = dict()
age = dict()
for i,nr in enumerate(nrs):
	if nr in spoken:
		age[nr] = spoken[nr]
	spoken[nr] = i
	# print("*",nr)

for i in range(i+1, 30000000):
	if nr not in age:
		nr = 0
	else:
		# print(f"{nr}: {spoken[nr]} {age[nr]}")
		nr = spoken[nr] - age[nr]
	
	if nr in spoken:
		age[nr] = spoken[nr]
	spoken[nr] = i
	# print(i, nr)
print(nr)