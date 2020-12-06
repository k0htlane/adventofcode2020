ret = 0
yes = set()
for line in open("input.txt"):
	line = line.strip()
	if line == "":
		print(yes)
		ret += len(yes)
		yes = set()
	else:
		yes |= set(line)
print(ret)