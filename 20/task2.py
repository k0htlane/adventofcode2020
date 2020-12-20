import sys
import re
import math
import numpy as np
from collections import namedtuple
import h5py

Sides = namedtuple("Sides", "left right bottom top")

class Tile:
	def __init__(self, data):
		header, *data = data.split("\n")
		self.id = int(re.match(r"Tile (\d+):", header)[1])
		self.data = np.array(list(map(list,data)))
		self.flips = [self._sides(i) for i in range(8)]

	def sides(self, flips):
		return self.flips[flips&7]

	def _sides(self, flips):
		data = self.data
		flips = flips&7
		if flips//2 == 1:
			data = np.rot90(data)
		elif flips//2 == 2:
			data = np.rot90(data, 2)
		elif flips//2 == 3:
			data = np.rot90(data, 3)

		if flips&1:
			data = np.fliplr(data)
		
		top = "".join(data[0, :])
		bottom = "".join(data[-1, :])
		left = "".join(data[:, 0])
		right = "".join(data[:, -1])
		return Sides(left, right, bottom, top)

class Row:
	def __init__(self, row):
		self.top = ""
		self.bottom = ""
		self.ids = []
		self.rot = []
		for i in row:
			tile = tiles[i//8].sides(i)
			self.bottom += tile.bottom
			self.top += tile.top
			self.ids.append(tiles[i//8].id)
			self.rot.append(i&7)
			# self.ids.append((tiles[i//8].id, i&3))
	
	def __str__(self):
		return str(self.ids)
		# return f"[{self.ids}]\n>>{self.top}\n>>{self.bottom}"
			

def check_left(this, left):
	tile_this = tiles[this//8].sides(this)
	tile_left = tiles[left//8].sides(left)
	return tile_this.left == tile_left.right


tiles = list(map(Tile, sys.stdin.read().split("\n\n")))
N = int(math.sqrt(len(tiles)))
print(len(tiles))
print(N)

def get_rows(row, tiles):
	if len(row) == N:
		rows.append(Row(row))
		return
	
	for t in tiles:
		for r in range(8):
			if len(row) == 0 or check_left(t*8+r, row[-1]):
				get_rows(row + [t*8+r], tiles - set([t]))
				

rows = []
get_rows([], set(range(N*N)))
print("rows=", len(rows))
for i,row in enumerate(rows):
	print(i,row)
# exit()

def check_rows(this, top, others):
	this, top = rows[this], rows[top]
	if this.top != top.bottom:
		return False
	topset = set(top.ids)
	for o in others:
		topset |= set(rows[o].ids)
	i = set(this.ids) & topset
	return len(i) == 0

def get_cols(col, avail):
	if len(col) == N:
		solutions.append(col)
		return
	
	for r in avail:
		if len(col) == 0 or check_rows(r, col[-1], col[:-1]):
			get_cols(col+[r], avail - set([r]))

solutions = []
get_cols([], set(range(len(rows))))

with h5py.File("solution.hdf5", "w") as file:
	file.create_dataset("rows", data=[row.ids for row in rows])
	file.create_dataset("rots", data=[row.rot for row in rows])
	file.create_dataset("solutions", data=solutions)

