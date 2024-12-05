import sys
from functools import cmp_to_key
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    rulesets_str, pages_str = f.read().split("\n\n")


# X|Y => X must be printed before Y
def parse_page_ordering_rules(rules):
    rulesets = []

    for line in rules.splitlines():
        x, y = map(int, line.split('|'))
        rulesets.append((x,y))

    return rulesets

rulesets = parse_page_ordering_rules(rulesets_str)

middle_sum = 0

pages = [list(map(int, line.split(','))) for line in pages_str.splitlines()]

# Task 1
for page in pages:
    ok = True
    for rule in rulesets:
        x, y = rule

        if (x not in page) or (y not in page):
            continue

        if page.index(x) > page.index(y):
            #print("Failed rule", rule, page)
            ok = False
            break

    if ok:
        mid = page[len(page)//2]
        #print("Adding", mid, page, rule)
        middle_sum += mid

print("Task 1:", middle_sum)

# Task 2 - now count only incorrect ones after re-ordering them

"""
Note: this comparison function is wrong! it doesn't do topological sort
It won't work for a case of:
    75, 97, 47, 61, 53
Because it provides:
    97, 75, 47, 61, 53
While it should provide:
    53, 61, 47, 75, 97
"""
@cmp_to_key
def sorting_func(x, y):
    for rule in rulesets:
        if (x, y) == rule:
            #print("Find", x, y)
            return y-x

    return 0


order = defaultdict(set)
for (before, after) in rulesets:
    order[before].add(after)

#for k, v in order.items():
#    print(k, "before", v)

@cmp_to_key
def cmp(a, b):
    if a in order[b]:
        #print("CmpA", a, b, order[b])
        return -1
    if b in order[a]:
        #print("CmpB", a, b, order[a])
        return 1
    return 0


middle_sum = 0
for page in pages:
    ok = False
    for rule in rulesets:
        x, y = rule

        if (x not in page) or (y not in page):
            continue

        if page.index(x) > page.index(y):
            #old_page = page
            #print(old_page)
            #page = sorted(page, key=sorting_func)
            page2 = sorted(page, key=cmp)
            #if page != page2:
            #    print(old_page, page, page2)
            #    asdf
            #print(old_page, "=>", page)
            ok = True
            break

    if ok:
        mid = page2[len(page)//2]
        #print("Adding", mid, page2, rule)
        middle_sum += mid

print("Task 2:", middle_sum)
