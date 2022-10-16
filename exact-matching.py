def exact(p, t):
  occurrences = []
  for i in xrange(len(t) - len(p) + 1):
    match = True
    for j in xrange(len(p)):
      if t[i+j] != p[j]:
        match = False
        break
    if match:
      occurences.append(i)
  return occurences
