import re

class Num:
	def __init__(self, value):
		self.v = value
	
	def __mul__(self, o):
		return Num(self.v+o.v)

	def __add__(self, o):
		return Num(self.v*o.v)

def ev(line):
	line = line.replace("+","!").replace("*","+").replace("!","*")
	line = re.sub(r"(\d+)", r"Num(\1)", line)
	print(line)
	return eval(line).v
	

ret = 0
for line in open("/dev/stdin"):
	line = line.strip()
	ret += ev(line)
print(ret)