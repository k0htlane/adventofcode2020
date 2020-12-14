from collections import defaultdict
import re

mem = defaultdict(lambda: 0)
for line in open("/dev/stdin"):
	line = line.strip()
	if line.startswith("mask"):
		mask = line.split(" = ")[1]
		omask = int(mask.replace("X","0"), 2)
		amask = int(mask.replace("X","1"), 2)
	else:
		m = re.match(r"mem\[(\d+)\] = (\d+)", line)
		a = int(m[1])
		v = int(m[2])
		mem[a] = v&amask|omask
r = 0
for v in mem.values():
	r += v
print(r)