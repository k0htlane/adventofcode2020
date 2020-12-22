import sys
import re

foods = []
ingrs = set()
allergs = set()
candidates = dict()
rcandidates = dict()
for line in sys.stdin:
	ingr, allerg = line.split(" (contains ")
	ingr = ingr.split(" ")
	allerg = allerg.split(", ")
	allerg[-1] = allerg[-1][:-2]
	foods.append((ingr, allerg))
	allergs |= set(allerg)
	ingrs |= set(ingr)
	for x in ingr:
		candidates[x] = set(allerg)
	for x in allerg:
		rcandidates[x] = set(ingr)

canbe = set()
def solve(solution, candidates, rcandidates, used, foods):
	global canbe
	if len(rcandidates) == 0:
		assert len(used) == len(allergs)
		r = sorted(list(solution.items()))
		f = lambda x: x[1]
		print(",".join(map(f, r)))
		return
	allerg, ingrs = rcandidates.popitem()
	for ingr in ingrs:
		if ingr in used:
			continue
		solution[allerg] = ingr
		candidates_ = dict()
		for key,val in candidates.items():
			if key != ingr:
				candidates_[key] = val - set([allerg])
		
		rcandidates_ = dict((k,v - set([ingr])) for k,v in rcandidates.items())

		foods_ = []
		try:
			for fi, fa in foods:
				fi = set(fi)
				fa = set(fa)
				if allerg in fa:
					fi.remove(ingr)
					fa.remove(allerg)
				foods_.append((fi, fa))
		except KeyError:
			continue

		sol = solve(solution, candidates_, rcandidates_, used | set([ingr]), foods_)
		# if sol:
			# return sol

# print(candidates)
# print(rcandidates)
solve(dict(), candidates, rcandidates, set(), foods)
