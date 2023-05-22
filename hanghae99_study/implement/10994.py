# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 차례대로 별을 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(readline())

    for i in range(2 * n - 1):
        if i == 0:
            print('*' * (4 * n - 3))
        elif i % 2 == 1:
            print('* ' * (i // 2 + 1), end='')
            print(' ' * (4 * (n - (i + 1) // 2) - 3), end='')
            print(' *' * (i // 2 + 1))
        else:
            print('* ' * (i // 2), end='')
            print('*' * (4 * (n - (i + 1) // 2) - 3), end='')
            print(' *' * (i // 2))
    for i in range(2 * n - 3, -1, -1):
        if i == 0:
            print('*' * (4 * n - 3))
        elif i % 2 == 1:
            print('* ' * (i // 2 + 1), end='')
            print(' ' * (4 * (n - (i + 1) // 2) - 3), end='')
            print(' *' * (i // 2 + 1))
        else:
            print('* ' * (i // 2), end='')
            print('*' * (4 * (n - (i + 1) // 2) - 3), end='')
            print(' *' * (i // 2))


solution()

# *****
# *   *
# * * *
# *   *
# *****

# 2

# *********
# *       *
# * ***** *
# * *   * *
# * * * * *
# * *   * *
# * ***** *
# *       *
# *********

# 3
