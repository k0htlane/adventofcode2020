import h5py
import numpy as np
import sys
import re

def readdata(data):
	return np.array([[1 if c=="#" else 0 for c in row] for row in data])

class Tile:
	def __init__(self, data):
		header, *data = data.split("\n")
		self.id = int(re.match(r"Tile (\d+):", header)[1])
		self.data = readdata(data)
	
	def image(self, flips):
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
		return data[1:-1,1:-1]

tiles = list(map(Tile, sys.stdin.read().split("\n\n")))
tiles = dict((tile.id, tile) for tile in tiles)


with h5py.File("solution.hdf5", "r") as file:
	rows = np.array(file["rows"])
	rots = np.array(file["rots"])
	solutions = np.array(file["solutions"])

def assemble(solution):
	ret = None
	for r in solution:
		row = None
		for t,f in zip(rows[r], rots[r]):
			if row is None:
				row = tiles[t].image(f)
			else:
				row = np.concatenate([row, tiles[t].image(f)], axis=1)
		if ret is None:
			ret = row
		else:
			ret = np.concatenate([ret, row], axis=0)
	return ret

seamonster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
seamonster = readdata(seamonster)

def find_seamonsters(solution):
	w,h = seamonster.shape
	roughness = solution.copy()
	for i in range(solution.shape[0]-seamonster.shape[0]):
		for j in range(solution.shape[1]-seamonster.shape[1]):
			view = solution[i:i+w,j:j+h]
			if np.all(view&seamonster == seamonster):
				# print(i,j)
				roughness[i:i+w,j:j+h] &= ~seamonster
	print(np.sum(roughness))

print(seamonster)
for solution in solutions:
	print("sol")
	solution = assemble(solution)
	find_seamonsters(solution)