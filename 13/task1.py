ts = int(input())
buses = []
for bus in  input().split(","):
	if bus == "x":
		pass
	else:
		buses.append(int(bus))

for bus in buses:
	nt = ts % bus
	print(ts - nt + bus, -nt + bus, bus)