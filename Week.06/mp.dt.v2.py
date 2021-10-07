# Distinct Triples Morning Problem
# n = 673
n = int(input())
k = 3
count = 0
for i in range(n):
    for j in range(i+1, n-1):
        more = (n - j  - 1)
        count += more
        if (j+1) >= (n-1):
            print(i, j, "%d : count %d (%d)" % (j+1, count, more))
        else:
            print(i, j, "%d-%d : count %d (%d)" % (j+1, n-1, count, more))
print(count)
