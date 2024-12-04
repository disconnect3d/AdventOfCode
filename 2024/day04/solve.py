import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

XMAS = 'XMAS'
XMAS_R = XMAS[::-1]

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count


def traverse_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Przekątne z lewego górnego do prawego dolnego
    diagonals_top_left_to_bottom_right = []
    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            j = d - i
            diagonal.append(matrix[i][j])
        diagonals_top_left_to_bottom_right.append(''.join(diagonal))

    # Przekątne z prawego górnego do lewego dolnego
    diagonals_top_right_to_bottom_left = []
    for d in range(-(cols - 1), rows):
        diagonal = []
        for i in range(max(0, d), min(rows, cols + d)):
            j = i - d
            diagonal.append(matrix[i][j])
        diagonals_top_right_to_bottom_left.append(''.join(diagonal))

    return diagonals_top_left_to_bottom_right, diagonals_top_right_to_bottom_left


def count_for_lines(lines):
    #for line in lines:
    #    print(line)
    cols, rows = len(lines[0]), len(lines)

    left_diag, right_diag = traverse_diagonals(lines)
    xmas = sum(occurrences(l, XMAS) + occurrences(l, XMAS_R) for l in lines)

    for chars in zip(*lines):
        l = ''.join(chars)
        xmas += occurrences(l, XMAS) + occurrences(l, XMAS_R)

    xmas += sum(occurrences(l, XMAS) + occurrences(l, XMAS_R) for l in left_diag)
    xmas += sum(occurrences(l, XMAS) + occurrences(l, XMAS_R) for l in right_diag)
    return xmas


#count_for_lines(['abcd', '1234', 'zxcv', '7890'])
xmas_count = count_for_lines(lines)
print("XMas count:", xmas_count)


def count_for_xmas(lines):
    cols, rows = len(lines[0]), len(lines)
    # Check for X-MAS pattern like:
    #  M.S
    #  .A.
    #  M.S
    check = lambda r, c: all((
        lines[r][c] == 'M', lines[r][c+2] == 'S',
        lines[r+1][c+1] == 'A',
        lines[r+2][c] == 'M', lines[r+2][c+2] == 'S'
    ))
    check2 = lambda r, c: all((
        lines[r][c] == 'S', lines[r][c+2] == 'M',
        lines[r+1][c+1] == 'A',
        lines[r+2][c] == 'S', lines[r+2][c+2] == 'M'
    ))
    check3 = lambda r, c: all((
        lines[r][c] == 'M', lines[r][c+2] == 'M',
        lines[r+1][c+1] == 'A',
        lines[r+2][c] == 'S', lines[r+2][c+2] == 'S'
    ))
    check4 = lambda r, c: all((
        lines[r][c] == 'S', lines[r][c+2] == 'S',
        lines[r+1][c+1] == 'A',
        lines[r+2][c] == 'M', lines[r+2][c+2] == 'M'
    ))
    #for line in lines:
    #    print(line)
    #print("==")

    counter = 0
    for r in range(rows-2):
        for c in range(cols-2):
            """
            print(r, c, lines[r][c:c+3])
            print(r, c, lines[r+1][c:c+3])
            print(r, c, lines[r+2][c:c+3])
            print('---', check(r, c))
            input()
            """
            if check(r,c) or check2(r,c) or check3(r,c) or check4(r,c):
                counter += 1
    return counter

print("Task 2:", count_for_xmas(lines))
