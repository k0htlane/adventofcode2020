from collections import defaultdict
import re

def write(mem, a, v, pmask):
	if len(pmask) == 0:
		mem[a] = v
		# print(bin(a|2**33),v)
	else:
		*pmask, l = pmask
		write(mem, a, v, pmask)
		write(mem, a|(1<<l), v, pmask)

mem = defaultdict(lambda: 0)
for line in open("/dev/stdin"):
	line = line.strip()
	if line.startswith("mask"):
		mask = line.split(" = ")[1]
		omask = int(mask.replace("X","0"), 2)
		amask = int(mask.replace("0","1").replace("X","0"), 2)
		pmask = [len(mask)-1-i for i,x in enumerate(mask) if x == "X"]
		# print(mask, pmask, amask, omask)
	else:
		m = re.match(r"mem\[(\d+)\] = (\d+)", line)
		a = int(m[1])
		v = int(m[2])
		# print(bin(a|2**33))
		a = a&amask|omask
		# print("write")
		# print(bin(a|2**33), v, "*")
		write(mem, a, v, pmask)
		# print("done")
r = 0
for v in mem.values():
	r += v

print(r)
print(r > 468487937448)
print(r > 1358338157334)