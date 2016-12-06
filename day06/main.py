#!/usr/bin/env python
from __future__ import print_function
from collections import Counter

def solve(text, cols=6, retrieval_func=lambda c: c.most_common(1)[0][0]):
    counters = tuple((Counter() for c in range(cols)))
    
    for line in text.split('\n'):
        for idx, char in enumerate(line):
            counters[idx].update(char)
    
    return ''.join(map(retrieval_func, counters))


testcase = ''.join((
    "eedadn\n",
    "drvtee\n",
    "eandsr\n",
    "raavrd\n",
    "atevrs\n",
    "tsrnev\n",
    "sdttsa\n",
    "rasrtv\n",
    "nssdts\n",
    "ntnada\n",
    "svetve\n",
    "tesnvt\n",
    "vntsnd\n",
    "vrdear\n",
    "dvrsen\n",
    "enarar\n"
))

assert solve(testcase) == 'easter'

with open('input.txt') as f:
    input_ = f.read()

print("Task1: ", solve(input_, cols=9)
print("Task2: ", solve(input_, cols=9, retrieval_func=lambda c: c.most_common()[-1][0][0])
