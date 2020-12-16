import re
lines = list(map(lambda l:l.strip(), open("/dev/stdin")))

ranges = []
def add_range(l, r):
	ranges.append((l,r))

rate = 0
for line in lines:
	m = re.match(r".+\: (\d+)-(\d+) or (\d+)-(\d+)", line)
	if m:
		add_range(int(m[1]), int(m[2]))
		add_range(int(m[3]), int(m[4]))
	elif line == "your ticket:":
		mode="your"
	elif line == "nearby tickets:":
		mode="nearby"
	elif line == "":
		pass
	elif mode == "your":
		pass
	elif mode == "nearby":
		for x in line.split(","):
			x = int(x)
			ok = False
			for l,r in ranges:
				if l <= x <= r:
					ok=True
					break
			if not ok:
				rate += x
	else:
		raise NotImplementedError(line)
print(rate)