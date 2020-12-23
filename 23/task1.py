cups = list(map(int, input().strip()))
maxcup = max(cups)

for i in range(100):
	cups, picked_up = cups[0:1] + cups[4:], cups[1:4]
	dest = cups[0]-1 if cups[0] > 1 else maxcup
	while dest in picked_up:
		dest -= 1
		if dest == 0:
			dest = maxcup
	idx = cups.index(dest)+1
	cups = cups[:idx] + picked_up + cups[idx:]
	cups = cups[1:] + cups[0:1]

idx = cups.index(1)
cups = cups[idx+1:] + cups[:idx]
print("".join(map(str, cups)))