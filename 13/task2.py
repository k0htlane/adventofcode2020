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
	print(i, i%buses == ofs, i%buses, ofs)
	for j,b in zip(ofs, buses):
		if (i+j)%b != 0:
			ok = False
			break
	if ok:
		print(i)
		exit()

buses = np.array(buses)
ofs = np.array(ofs)%buses

# idx = np.argsort(buses)
# buses = buses[idx]
# ofs = ofs[idx]

print(buses)
print(ofs)

t = 0
x = 1
for i in range(0, len(buses)):
	print(f"i={i} t={t} x={x} : {t}%{buses[i]} {t%buses[i]} != {ofs[i]}")

	while t%buses[i] != ofs[i]:
		t += x
	print(t%buses-ofs, f"({t})")
	# print(ofs)
	print()
	# x = np.lcm(x, buses[i])
	x = x*buses[i]

print(f"x={x}")
print(f"t={t}")
# print(x-t + ofs.max())
print(buses)
print(ofs)

for i in range(0, ofs.max()+1):
	check(x-t+i)
	# assert x-t+i != 1068781
		          # 1068781
check(t)
# print(t, t+x)
# print("RUNNING")
# while True:
	# check(t)
	# t += x

# 1068781
# 3162341