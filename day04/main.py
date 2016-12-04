#!/usr/bin/env python
from __future__ import print_function
from collections import defaultdict
from string import ascii_letters


def parse(line):
    last_dash_idx = line.rindex('-')
    bracket_idx = line.index('[')
    
    return {
        'room': line[:last_dash_idx],
        'sector_id': int(line[last_dash_idx+1:bracket_idx]),
        'checksum': line[bracket_idx+1:-1]
    }


def is_valid_checksum(room, checksum):
    letters = defaultdict(lambda: 0)
    
    for c in room:
        if c == '-':
            continue
        letters[c] += 1
    
    top_sorted = list(letters.items())
    # thanks to this sorting key, items will be sorted by scores and then alphabetically
    top_sorted.sort(key=lambda i: (i[1], (1000-ord(i[0]))), reverse=True)
    
    top_five = ''.join(i[0] for i in top_sorted[:5])
    return top_five == checksum


def solve(rooms):
    return sum(
        d['sector_id'] for d in map(parse, rooms) if is_valid_checksum(d['room'], d['checksum'])
    )


testcase = (
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
)


def decrypt_room_name(room, sector_id):
    return ''.join(
        ascii_letters[(ascii_letters.index(ch)+sector_id)%len(ascii_letters)] if ch != '-' else ' ' for ch in room
    ).lower()


with open('input.txt') as f:
    rooms = f.read().split('\n')
    
print("Task 1")
assert solve(testcase) == 1514
print ("Task 1 solution =", solve(rooms))

    

print("Task 2")
assert decrypt_room_name('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'
decrypted = [
    (decrypt_room_name(d['room'], d['sector_id']), d['sector_id']) for d in map(parse, rooms)
]
print("Task 2 - Decrypted that contains 'north':")
print(list(filter(lambda i: 'north' in i[0], decrypted)))
