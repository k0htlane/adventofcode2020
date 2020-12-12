x, y = 0, 0
wx, wy = 10, 1
di = "E"
vecs = dict(E=(1,0), W=(-1,0), N=(0,1), S=(0,-1))
lefts = "WSEN"
rights = lefts[::-1]
for line in open("test.txt"):
	line = line.strip()
	arg = int(line[1:])
	cmd = line[0]
	
	if cmd in vecs:
		dx, dy = vecs[cmd]
		wx += dx*arg
		wy += dy*arg
	elif cmd == "F":
		x += wx*arg
		y += wy*arg
	elif cmd == "L":
		dx, dy = 0, 0
		for _ in range(arg//90):
			wx, wy = -wy, wx
	elif cmd == "R":
		dx, dy = 0, 0
		for _ in range(arg//90):
			wx, wy = wy, -wx


print(abs(x)+abs(y))