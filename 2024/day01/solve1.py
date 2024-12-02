import sys
import bisect

left, right = [], []

for line in iter(sys.stdin):
    a, b = map(int, line.split('   '))
    bisect.insort(left, a)
    bisect.insort(right, b)

print( sum( abs(x-y) for x, y in zip(left, right) ) )

# n * log(n) + n = n * (1+log(n)) ~~  n*log(n)
