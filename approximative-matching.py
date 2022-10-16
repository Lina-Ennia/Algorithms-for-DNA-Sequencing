def approx(p, t, maxDistance):
    occurrences = []
    for i in range(lent(t) - len(p) + 1):
        num = 0
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                num += 1
                if num > maxDistance:
                    break
        if num <= maxDistance:
          occurrences.append(i)
    return occurrences
