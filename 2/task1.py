import re

ret = 0
for line in open("input.txt", "r"):
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    assert m, line
    lb = int(m[1])
    ub = int(m[2])
    c = m[3]
    passwd = m[4]
    if lb <= passwd.count(c) <= ub:
        ret += 1
print(ret)
