ret = 0
yes = set()
for line in open("input.txt"):
	line = line.strip()
	if line == "":
		# Note that for this data, I added one more line at the end of input.txt, so
		# that this if is always entered at the end of the file.
		print(yes)
		ret += len(yes)
		yes = set()
	else:
		yes |= set(line)
print(ret)