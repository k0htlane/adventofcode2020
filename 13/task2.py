from time import monotonic
import numpy as np

ts = int(input())
buses = []
ofs = []
for i,bus in enumerate(input().split(",")):
	if bus == "x":
		pass
	else:
		buses.append(int(bus))
		ofs.append(i)

def check(i):
	ok = True
	for j,b in zip(ofs, buses):
		if (i+j)%b != 0:
			ok = False
			break
	if ok:
		print(i)
		exit()

buses = np.array(buses)
ofs = np.array(ofs)%buses


t = 0
x = 1
for i in range(0, len(buses)):

	while t%buses[i] != ofs[i]:
		t += x
	x = x*buses[i]


check(x-t) # no clue why x-t, but it works, so ¯\_(ツ)_/¯
