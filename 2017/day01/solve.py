import sys


def solve(data):
    length = len(data)
    last_num = data[0]
    sum_val = 0

    for i in range(1, length+1):
        num = data[i % length]

        if num == last_num:
            sum_val += num
        last_num = num

    return sum_val


def solve2(data):
    length = len(data)
    offset = int(length / 2)
    sum_val = 0

    for i in range(1, len(data)+1):
        num = data[i % length]

        if num == data[(i+offset) % length]:
            sum_val += num

    return sum_val

for d in ((1, 1, 2, 2), (1, 1, 1, 1), (1, 2, 3, 4), (9, 1, 2, 1, 2, 1, 2, 9)):
    print(d, '=', solve(d))

with open(sys.argv[1]) as input_file:
    data = map(int, input_file.read().rstrip())
    print('result1 =', solve(data))
    print('result2 =', solve2(data))

