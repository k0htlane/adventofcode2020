from collections import defaultdict
import re

def write(mem, a, v, pmask):
	if len(pmask) == 0:
		mem[a] = v
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
	else:
		m = re.match(r"mem\[(\d+)\] = (\d+)", line)
		a = int(m[1])
		v = int(m[2])
		a = a&amask|omask
		write(mem, a, v, pmask)
r = 0
for v in mem.values():
	r += v

print(r)
