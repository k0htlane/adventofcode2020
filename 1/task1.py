f = open("input.txt", "r")
numbers = list(map(int, f))
for a in numbers:
  for b in numbers:
    if a+b == 2020:
      print(a*b, a, b)