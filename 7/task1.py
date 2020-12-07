import re
from collections import defaultdict

def parse_line(line):
	m = re.match(r"^(\w+(\s\w+)*) bags? contain no other bags.$", line)
	if m:
		return m[1], []

	m = re.match(r"(\w+(?:\s\w+)*) bags? contain ", line)
	kind = m[1]
	contain = []

	while True:
		line = line[m.end():]
		m = re.match(r"^(\d+) (\w+(?:\s\w+)*) bags?(, |\.)", line)
		# print(line, m)
		contain.append((int(m[1]), m[2]))
		if m[3] == ".":
			return kind, contain

	# m = re.match(r"^(\w+(?:\s\w+)*) contain (\d+) (\w+(?:\s\w+)*) bags?(, (\d+) (\w+(?:\s\w+)*) bags?)*.$", line)
	# kind, *g = list(m.groups())
	# print(kind, g)
	# ret = []
	# for i in range(len(g)//2):
	# 	if g[i*2+1] is None:
	# 		break
	# 	ret.append((int(g[i*2]), g[i*2+1].replace(" bags", "").replace(" bag","")))
	# return kind.replace(" bags", "").replace(" bag",""), ret

graph = defaultdict(set)

for line in open("input.txt"):
	line = line.strip()
	# print(line)
	kind, contain = parse_line(line)
	# print(kind, contain)
	# input()

	for n, k in contain:
		graph[k].add(kind)
		# print(k, ">-->", kind)
# print()
visited = set()
queue = ["shiny gold"]
ret = 0
while len(queue) > 0:
	color = queue.pop(0)
	ret += 1
	print(color)
	for edge in graph[color]:
		if edge not in visited:
			# print(color, ">>", edge)
			queue.append(edge)
			visited.add(edge)
print(ret-1)

