ip = 0
code = []
visited = []

for line in open("input.txt"):
	op, arg = line.strip().split(" ")
	code.append((op, int(arg)))
	visited.append(False)

acc = 0
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
print(acc)
