import sys
a = [str(float(i)) for i in sys.argv[1:]]

def f(n):
  l = len(n)

  if l == 1 and eval(n[0]) == 24:
    print n[0]
    
  k = range(l)
  for i in k:
    for j in k:
      if i != j:
        for o in '+-*/':
          m = list(n)
          m[i] = '('+n[i]+o+n[j]+')'
          del m[j]
          if o != '/' or eval(n[j]) != 0:
            f(m)
f(a)
