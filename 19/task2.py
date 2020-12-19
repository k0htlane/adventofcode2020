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

class Multiple:
	def __init__(self, a, b):
		self.solutions = []
		if isinstance(a, Multiple):
			self.solutions += a.solutions
		else:
			self.solutions.append(a)
		if isinstance(b, Multiple):
			self.solutions += b.solutions
		else:
			self.solutions.append(b)
	
	def filter(self, s):
		ret = []
		for sol in self.solutions:
			if sol == "":
				continue
			if sol[0] == s:
				ret.append(sol[1:])
		if len(ret) == 0:
			return None
		if len(ret) == 1:
			return ret[0]
		m = Multiple(None, None)
		m.solutions = ret
		return m
	
	def __eq__(self, other):
		raise NotImplementedError

	def empty(self):
		return all(x=="" for x in self.solutions)

# @logger
def match(line, rule):
	if isinstance(line, Multiple):
		if line.empty():
			return None
	elif line == "":
		return None
	if isinstance(rule, list):
		for r in rule:
			line = match(line, rules[r])
			if line is None:
				return
		return line
	elif isinstance(rule, tuple):
		m1 = match(line, rule[0])
		m2 = match(line, rule[1])
		if m1 is not None and m2 is not None:
			return Multiple(m1, m2)
		return m2 if m1 is None else m1
	elif isinstance(rule, str):
		if isinstance(line, Multiple):
			return line.filter(rule)
		elif line[0] == rule:
			return line[1:]
	else:
		raise NotImplementedError

rules[8] = [42], [42, 8]
rules[11] = [42, 31], [42, 11, 31]

# print(rules)
ret = 0
for line in sys.stdin:
	line = line.strip()
	# print("##", line)
	m = match(line, rules[0])
	if isinstance(m, Multiple):
		if "" in m.solutions:
			ret += 1
	elif m == "":
		ret += 1
	# break
print(ret)
assert(ret > 216)