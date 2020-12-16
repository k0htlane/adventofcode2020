import re
lines = list(map(lambda l:l.strip(), open("/dev/stdin")))

fields = dict()
rate = 0
tickets = []
all_ranges = []
for line in lines:
	m = re.match(r"(.+)\: (\d+)-(\d+) or (\d+)-(\d+)", line)
	if m:
		l1, r1 = int(m[2]), int(m[3])
		l2, r2 = int(m[4]), int(m[5])
		fields[m[1]] = [(l1,r1), (l2,r2)]
		all_ranges += [(l1,r1), (l2,r2)]
	elif line == "your ticket:":
		valids = [set(fields.keys()) for i in range(len(fields))]
		mode="your"
	elif line == "nearby tickets:":
		mode="nearby"
	elif line == "":
		pass
	else:
		if mode == "your":
			myticket = (list(map(int, line.split(","))))
		
		valid_ticket = True
		for i,x in enumerate(line.split(",")):
			x = int(x)

			ok = False
			for l,r in all_ranges:
				if l <= x <= r:
					ok = True
					break
			if not ok:
				valid_ticket = False

		if not valid_ticket:
			continue

		for i,x in enumerate(line.split(",")):
			x = int(x)
			for name,ranges in fields.items():
				if name not in valids[i]:
					continue
				ok = False
				for l,r in ranges:
					if l <= x <= r:
						ok = True
						break
				if not ok:
					if i == 0:
						print(f"{i} remove {name} ({x} not in {ranges})")
					valids[i].remove(name)

unsolved = set(range(len(valids)))
solved = set()
fieldmap = dict()
while len(unsolved) > 0:
	for i in unsolved:
		valids[i] = valids[i] - solved
		if len(valids[i]) == 1:
			sol, = valids[i]
			unsolved.remove(i)
			solved.add(sol)
			fieldmap[sol] = i
			break
print(fieldmap)
ret = 1
for field,pos in fieldmap.items():
	if field.startswith("departure"):
		ret *= myticket[pos]
print(ret)