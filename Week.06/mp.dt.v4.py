# Distinct Triples Morning Problem
import math
n = int(input())
k = 3                       # Not used.  Implied.
f1_count = math.factorial(n) / (6 * math.factorial(n-3))
f1_count = int(f1_count)
print("Formula 1: ", f1_count)

f2_count = (n*(n-1)*(n-2)) / 6
f2_count = int(f2_count)
print("Formula 2: ", f2_count)
