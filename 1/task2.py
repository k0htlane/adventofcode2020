f = open("input.txt", "r")
numbers = list(map(int, f))
for a in numbers:
  for b in numbers:
    for c in numbers:
      if a+b+c == 2020:
        print(a*b*c, a, b,c)