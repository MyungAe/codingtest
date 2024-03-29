# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    repeat_count = int(readline())

    dp = [0 for _ in range(11)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for _ in range(repeat_count):
        target = int(readline())

        # 채우는 과정
        for index in range(3, target):
            dp[index] = dp[index - 1] + dp[index - 2] + dp[index - 3]

        # print(dp)
        print(dp[target - 1])


solution()


# 7
# 44
# 274

# 3
# 4
# 7
# 10
