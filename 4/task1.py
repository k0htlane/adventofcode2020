def process(lines):
	fields = dict()
	for line in lines:
		for kv in line.split(" "):
			k, v = kv.split(":")
			fields[k] = v
	for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
		if k not in fields:
			return 0
	return 1

ret = 0
lines = []
for line in open("input.txt", "r"):
	line = line.strip()
	if line == "":
		ret += process(lines)
		lines = []
	else:
		lines.append(line)
		
ret += process(lines)
print(ret)
