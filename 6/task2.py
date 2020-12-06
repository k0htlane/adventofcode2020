ret = 0
yes = set("qwertyuiopasdfghjklzxcvbnm")
for line in open("input.txt"):
	line = line.strip()
	if line == "":
		ret += len(yes)
		yes = set("qwertyuiopasdfghjklzxcvbnm")
	else:
		yes &= set(line)
print(ret)