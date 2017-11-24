from __future__ import print_function
from __future__ import division
import itertools


def is_triangle(a, b, c):
    return a+b>c and a+c>b and b+c>a


with open('input.txt') as f:
    data = f.read()


print("Task 1")
lines = data.splitlines()
triangles_sides = list(map(lambda i: list(map(int, i.split())), lines))
are_triangles = [is_triangle(*sides) for sides in triangles_sides]
triangles_count = sum(are_triangles)

# Above could be written as a one liner, however not really readable:
# triangles_count = sum(is_triangle(*sides) for sides in map(lambda i: map(int, i.split()), data.split('\n')))
print("Triangles count:", triangles_count)


print("Task 2")
triples_count = int(len(triangles_sides)/3)
triple_row_triangles = [triangles_sides[i*3:i*3+3] for i in range(triples_count)]
transposed_triangles = [zip(*i) for i in triple_row_triangles]
triangles_count = sum(is_triangle(*sides) for sides in itertools.chain(*transposed_triangles))
print("Triangles count:", triangles_count)
