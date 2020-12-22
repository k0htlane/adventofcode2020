import re
import numpy as np
import sys

def parse(deck):
	return list(map(int, deck.split("\n")[1:]))
p1, p2 = list(map(parse, sys.stdin.read().split("\n\n")))

def play(win, lose):
	a = win.pop(0)
	b = lose.pop(0)
	win.append(a)
	win.append(b)


while len(p1) > 0 and len(p2) > 0:
	if p1[0] > p2[0]:
		play(p1, p2)
	else:
		play(p2, p1)

for hand in [p1, p2]:
	ret = 0
	for m,c in enumerate(hand[::-1]):
		ret += (m+1)*c
	print(ret)