import sys

def parse(line):
	ret = []
	while len(line) > 0:
		if line.startswith("e"):
			ret.append((1,0))
			line = line[1:]
		elif line.startswith("w"):
			ret.append((-1,0))
			line = line[1:]
		elif line.startswith("sw"):
			ret.append((-0.5,-0.5))
			line = line[2:]
		elif line.startswith("se"):
			ret.append((0.5,-0.5))
			line = line[2:]
		elif line.startswith("nw"):
			ret.append((-0.5,0.5))
			line = line[2:]
		elif line.startswith("ne"):
			ret.append((0.5,0.5))
			line = line[2:]
	return ret

flipped_tiles = set()
for line in sys.stdin:
	line = line.strip()
	pos = (0, 0.)
	for dx,dy in parse(line):
		pos = pos[0]+dx, pos[1]+dy
	if pos not in flipped_tiles:
		flipped_tiles.add(pos)
	else:
		flipped_tiles.remove(pos)
print(len(flipped_tiles))