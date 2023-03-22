# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    columns = int(readline())
    dp = [0 for _ in range(1001)]

    dp[0] = 1
    dp[1] = 1

    for index in range(2, columns + 1):
        dp[index] = dp[index - 1] + 2 * dp[index - 2]

    return dp[columns] % 10007


print(solution())

# 3

# 2

# 171

# 8

# 2731

# 12
