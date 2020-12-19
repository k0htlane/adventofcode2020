import sys
import re

rules = dict()
for line in sys.stdin:
	line = line.strip()
	if line == "":
		break
	
	m1 = re.match(r"(\d+): \"(\w)\"", line)
	m2 = re.match(r"(\d+):((?: \d+)+)", line)
	m3 = re.match(r"(\d+):((?: \d+)+) \|((?: \d+)+)", line)
	if m1:
		rule = int(m1[1])
		rules[rule] = m1[2]
	elif m3:
		rule = int(m3[1])
		or1 = list(int(x) for x in m3[2].split())
		or2 = list(int(x) for x in m3[3].split())
		rules[rule] = or1, or2
	elif m2:
		rule = int(m2[1])
		rules[rule] = list(int(x) for x in m2[2].split())

def logger(fn):
	def inner(*a):
		r = fn(*a)
		print(f"match({a}) = {r}")
		return r
	return inner

# @logger
def match(line, rule):
	if isinstance(rule, list):
		for r in rule:
			line = match(line, rules[r])
			if line is None:
				return
		return line
	elif isinstance(rule, tuple):
		m = match(line, rule[0])
		if m is not None:
			return m
		else:
			return match(line, rule[1])
	elif isinstance(rule, str):
		if line[0] == rule:
			return line[1:]
	else:
		raise NotImplementedError

print(rules)
ret = 0
for line in sys.stdin:
	line = line.strip()
	# print("##", line)
	if match(line, rules[0]) == "":
		ret += 1
	# break
print(ret)