#!/usr/bin/env python

from __future__ import print_function
import enum
import numpy as np

d = enum.Enum('Direction', ('N', 'E', 'W', 'S'))
directions = (d.N, d.E, d.S, d.W)


def make_turn(direction, turn):
    idx = directions.index(direction)
    return directions[ idx-1 if turn == 'L' else (idx+1) % len(directions) ]


def taxicab_distance(p1, p2):
    return sum(map(abs, p2-p1))


def solve(movements):
    end_pos = np.array((0, 0))
    direction = d.N
        
    direction_to_axis_step = {
        d.N: np.array((0, 1)),
        d.E: np.array((1, 0)),
        d.W: np.array((-1, 0)),
        d.S: np.array((0, -1))
    }

    for movement in movements.split(', '):
        turn = movement[0]
        steps = int(movement[1:])

        direction = make_turn(direction, turn)
        end_pos += direction_to_axis_step[direction] * steps

    return taxicab_distance((0, 0), end_pos)


# testcases
assert solve("R2, L3") == 5
assert solve("R2, R2, R2") == 2
assert solve("R5, L5, R5, R3") == 12

print("Teh solution is", solve("R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"))
