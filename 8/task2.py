import copy
code = []

for line in open("input.txt"):
	op, arg = line.strip().split(" ")
	code.append([op, int(arg)])

def run(code):
	visited = [False] * len(code)
	acc = 0
	ip = 0
	while not visited[ip]:
		op, arg = code[ip]
		# print(ip, op, arg)
		visited[ip] = True
		if op == "acc":
			ip += 1
			acc += arg
		elif op =="jmp":
			ip += arg
		elif op == "nop":
			ip += 1

		if ip == len(code):
			print(acc)
			exit(0)

for i in range(len(code)):
	code_copy = copy.deepcopy(code)
	if code[i][0] == "jmp":
		code_copy[i][0] = "nop"
		run(code_copy)
		assert code[i][0] == "jmp"
	elif code[i][0] == "nop":
		code_copy[i][0] = "jmp"
		run(code_copy)