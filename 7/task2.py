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

graph = defaultdict(list)

for line in open("input.txt"):
	line = line.strip()
	kind, contain = parse_line(line)
	for n, k in contain:
		graph[kind].append((n, k))

def handbags(bag, N=1):
	global graph
	ret = N
	for n,k in graph[bag]:
		ret += N*handbags(k,n)
	return ret

print(handbags("shiny gold")-1)