import re
import numpy as np
import sys

def parse(deck):
	return list(map(int, deck.split("\n")[1:]))
p1, p2 = list(map(parse, sys.stdin.read().split("\n\n")))

# seen1, seen2 = set(), set()

class Combat:
	def __init__(self, p1, p2, level=0):
		self.hands = list(p1), list(p2)
		self.seen1 = set()
		self.seen2 = set()
		self.level = level
	
	def play_hand(self):
		a = self.hands[0].pop(0)
		b = self.hands[1].pop(0)

		if len(self.hands[0]) >= a and len(self.hands[1]) >= b:
			r = Combat(self.hands[0][:a], self.hands[1][:b], self.level+1)
			winner = r.play()
		else:
			winner = 0 if a > b else 1
		
		if winner == 0:
			self.hands[0].append(a)
			self.hands[0].append(b)
		elif winner == 1:
			self.hands[1].append(b)
			self.hands[1].append(a)


	def play(self):
		# print(self.level*"-", *self.hands)
		while all(map(lambda x: len(x)>0, self.hands)):
			h1 = tuple(self.hands[0])
			h2 = tuple(self.hands[1])
			if h1 in self.seen1 and h2 in self.seen2:
				return 0
			self.seen1.add(h1)
			self.seen2.add(h2)
			self.play_hand()
			# print(self.level*"-", *self.hands)
		return 0 if len(self.hands[1]) == 0 else 1
		

cards = Combat(p1, p2)
print("winner=", cards.play())
print(cards.hands)

for hand in cards.hands:
	ret = 0
	for m,c in enumerate(hand[::-1]):
		ret += (m+1)*c
	print(ret)