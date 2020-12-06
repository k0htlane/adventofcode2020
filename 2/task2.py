import re

ret = 0
for line in open("input.txt", "r"):
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    assert m, line
    lb = int(m[1])
    ub = int(m[2])
    c = m[3]
    passwd = m[4]
    cond1 = passwd[lb-1] == c
    cond2 = passwd[ub-1] == c
    if cond1 ^ cond2:
        ret += 1
print(ret)
