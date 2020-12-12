x, y = 0, 0
di = "E"
vecs = dict(E=(1,0), W=(-1,0), N=(0,1), S=(0,-1))
lefts = "WSEN"
rights = lefts[::-1]
for line in open("input.txt"):
	line = line.strip()
	arg = int(line[1:])
	cmd = line[0]
	
	if cmd in vecs:
		dx, dy = vecs[cmd]
	elif cmd == "F":
		dx, dy = vecs[di]
	elif cmd == "L":
		dx, dy = 0, 0
		for _ in range(arg//90):
			i = lefts.index(di)
			di = lefts[(i+1)%4]
	elif cmd == "R":
		dx, dy = 0, 0
		for _ in range(arg//90):
			i = rights.index(di)
			di = rights[(i+1)%4]


	x += dx*arg
	y += dy*arg
	# print(line, x,y)

print(abs(x)+abs(y))