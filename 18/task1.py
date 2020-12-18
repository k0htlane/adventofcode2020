import re

def evo(l, op, r):
	# print(l, op, r)
	if op == "+":
		return l+r
	elif op == "*":
		return l*r
	elif op == "/":
		return l/r
	elif op == "-":
		return l-r
	else:
		return NotImplementedError

def ev(code):
	code = re.split(r"( |\(|\))", code)
	op = [None] * 64
	val = [None] * 64
	i = 0
	for tok in code:
		if tok == "" or tok == " ":
			continue
		if tok in "+-*/":
			op[i] = tok
		elif tok == "(":
			i += 1
			val[i] = None
			op[i] = None
		elif tok == ")":
			i -= 1
			if op[i] is None:
				val[i] = val[i+1]
			else:
				val[i] = evo(val[i], op[i], val[i+1])
		elif op[i] is None:
			val[i] = int(tok)
		else:
			val[i] = evo(val[i], op[i], int(tok))
	# print("==>", val[0])
	return val[0]

ret = 0
for line in open("/dev/stdin"):
	line = line.strip()
	ret += ev(line)
print(ret)