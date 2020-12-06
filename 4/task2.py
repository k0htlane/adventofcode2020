import re

#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
#    cid (Country ID) - ignored, missing or not.

def valid_byr(x):
	return len(x) == 4 and 1920 <= int(x) <= 2002
def valid_iyr(x):
	return len(x) == 4 and 2010 <= int(x) <= 2020
def valid_eyr(x):
	return len(x) == 4 and 2020 <= int(x) <= 2030

def valid_hgt(x):
	if x.endswith("cm"):
		return 150 <= int(x[:-2]) <= 193
	elif x.endswith("in"):
		return 59 <= int(x[:-2]) <= 76
	return False

def valid_hcl(x):
	return None != re.match(r"#[0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z]", x)

def valid_ecl(x):
	return x in "amb blu brn gry grn hzl oth"

def valid_pid(x):
	return len(x) == 9 and None != re.match(r"[0-9]+", x)

def process(lines):
	fields = dict()
	for line in lines:
		for kv in line.split(" "):
			k, v = kv.split(":")
			fields[k] = v
	for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
		# valid = globals().get("valid_"+k, lambda x: True)
		valid = globals().get("valid_"+k, None)
		if k not in fields or not valid(fields[k]):
			return 0
		#del fields[k]
	#print(fields["pid"])
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
