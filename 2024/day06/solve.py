import sys, copy

"""
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.
"""

game_map = [list(line) for line in open(sys.argv[1], "r").read().splitlines()]
game_map_copy = copy.deepcopy(game_map)

rows = len(game_map)
cols = len(game_map[0])

OBSTRUCTION = '#'
NONE = '.'
UP, RIGHT, DOWN, LEFT = '^', '>', 'v', '<'

# turn right 90 degrees
TURNS = {
    UP:     RIGHT,
    RIGHT:  DOWN,
    DOWN:   LEFT,
    LEFT:   UP,
}

# (dy, dx)
POSITION_DELTAS = {
    UP:     (-1, 0),
    RIGHT:  (0, 1),
    DOWN:   (1, 0),
    LEFT:   (0, -1)
}


def find_char(char):
    for y in range(rows):
        for x in range(cols):
            if game_map[y][x] == char:
                return y, x

    raise ValueError(f'Char {char} not found on game map')


def print_map():
    print('-------------------')
    for r in range(rows):
        print(' '.join(game_map[r][c] for c in range(cols)))

visited_cells = set()
guard_dir = UP  # Assuming guard starts on UP direction
guard_pos = find_char(guard_dir)

while True:
    #input()
    #print_map()

    # Compute next guard position
    dy, dx = POSITION_DELTAS[guard_dir]
    y, x = guard_pos

    forward_y = y + dy
    forward_x = x + dx

    # If we fall out of map, break!
    if forward_y < 0 or forward_y == rows or forward_x < 0 or forward_x == cols:
        visited_cells.add(guard_pos)
        break

    # If there is an obstruction, rotate guard (update its direction)
    if game_map[forward_y][forward_x] == OBSTRUCTION:
        guard_dir = TURNS[guard_dir]

    # Else, update map, save visited cell and update guard position
    else:
        game_map[y][x] = NONE
        game_map[forward_y][forward_x] = guard_dir

        visited_cells.add(guard_pos)
        guard_pos = (forward_y, forward_x)

print("Guard visited cells:", len(visited_cells))

"""
--- Part Two ---
While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...

(...)
"""

"""
Task 2:
We can do this on each guard step: find the next path of guard and see if it would loop?
"""
del visited_cells  # not related to task 2

# When we are in simulation, we still play the game but without simulating loops
# now if the guard got to any of the same position and direction as after the simulation started = its a loop!
# or if we finished game simulating => its not a loop

# Game states
# SIMULATING        - we are now simulating the game in all ticks
# AFTER_SIMULATION  - we finished simulation and make one step without simulation
# TO_BE_SIMULATED   - we will be entering simulation in next tick
SIMULATING = 'SIMULATING'
AFTER_SIMULATION = 'AFTER SIM'
TO_BE_SIMULATED = 'TO BE SIM'

# State transitions:
# TO_BE_SIMULATED -> SIMULATING
# SIMULATING -> AFTER_SIMULATION
# AFTER_SIMULATION -> TO_BE_SIMULATED

loop_simulation_state = TO_BE_SIMULATED

guard_dir_before_simulation = UP
guard_pos_before_simulation = (999999, 99999)
loop_candidate = (99999, 999999)

# (y, x, dir) of visited simulated guard positions and directions
# this must be clear
simulation_visited_posdirs = set()

checked_loop_candidates = []
found_loop_positions = set()

# State to revert after simulation:
# guard_dir, guard_pos, game_map[fy][fx], game_map (old guard pos, new guard pos), simulation_visited_posdirs


DEBUG = len(sys.argv)>3


def enter_simulation():
    global loop_simulation_state, guard_dir_before_simulation, guard_pos_before_simulation, loop_candidate
    game_map[forward_y][forward_x] = OBSTRUCTION
    
    guard_dir_before_simulation = guard_dir
    guard_pos_before_simulation = guard_pos

    loop_candidate = (forward_y, forward_x)
    checked_loop_candidates.append(loop_candidate)

    y,x = guard_pos
    if all((
        game_map[y+1][x] == OBSTRUCTION,
        game_map[y-1][x] == OBSTRUCTION,
        game_map[y][x+1] == OBSTRUCTION,
        game_map[y][x-1] == OBSTRUCTION,
        )):
        print("WTF?")
        print_state()

    loop_simulation_state = SIMULATING
    if DEBUG:
        print("Entered simulation")


def exit_simulation():
    global guard_dir, guard_pos, loop_simulation_state

    # Revert state to the one before simulation
    y, x = guard_pos_before_simulation
    game_map[y][x] = guard_dir_before_simulation

    oy, ox = loop_candidate
    game_map[oy][ox] = NONE
    game_map[guard_pos[0]][guard_pos[1]] = NONE

    guard_dir = guard_dir_before_simulation
    guard_pos = guard_pos_before_simulation

    simulation_visited_posdirs.clear()

    loop_simulation_state = AFTER_SIMULATION
    if DEBUG:
        print("Exitted simulation")


# Reset game map for task 2
game_map = game_map_copy
guard_dir = UP  # Assuming guard starts on UP direction
guard_pos = find_char(guard_dir)

def print_state():
    print_map()
    print("Sim:", loop_simulation_state)


while True:
    # Compute next guard position
    dy, dx = POSITION_DELTAS[guard_dir]
    y, x = guard_pos

    forward_y = y + dy
    forward_x = x + dx

    if DEBUG:
        input()
        print_state()

    # If we fall out of map, exit simulation or break!
    if forward_y < 0 or forward_y == rows or forward_x < 0 or forward_x == cols:

        # Exit simulation, revert state, transition to AFTER_SIMULATION
        if loop_simulation_state == SIMULATING:
            exit_simulation()
            continue

        break

    # If there is an obstruction, rotate guard (update its direction)
    if game_map[forward_y][forward_x] == OBSTRUCTION:
        guard_dir = TURNS[guard_dir]

    # If to be simulated -- enter simulation
    elif loop_simulation_state == TO_BE_SIMULATED:
        enter_simulation()

    # If we are simulating, check if the current pos is already visited: if it is, it is a loop
    elif loop_simulation_state == SIMULATING and (guard_dir, y, x) in simulation_visited_posdirs:
        found_loop_positions.add(loop_candidate)
        if DEBUG:
            print("Found valid loop position!:", loop_candidate)
        exit_simulation()

    # Else just update map, save visited cell and update guard position
    else:
        if loop_simulation_state == AFTER_SIMULATION:
            loop_simulation_state = TO_BE_SIMULATED
        elif loop_simulation_state == SIMULATING:
            simulation_visited_posdirs.add( (guard_dir, y, x) )

        game_map[y][x] = NONE
        game_map[forward_y][forward_x] = guard_dir
        guard_pos = (forward_y, forward_x)

print("Found loop candidates", len(found_loop_positions))
