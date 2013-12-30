import itertools as t

a = raw_input().split()

for i in t.permutations(a + list('()+-*/'* (len(a)-1)), 7):
  try:
    s = ''.join(i)
    r = eval(s)
    if r == 24:
      print s

  except:
    0
