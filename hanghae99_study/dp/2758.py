# 선영이는 매주 엄청난 돈을 로또에 투자한다. 선영이가 하는 로또는 1부터 m까지 숫자 중에 n개의 수를 고르는 로또이다.
# 이렇게 열심히 로또를 하는데, 아직까지 한 번도 당첨되지 않은 이유는 수를 고를 때 각 숫자는 이전에 고른 수보다 적어도 2배가 되도록 고르기 때문이다.
# 예를 들어, n=4, m=10일 때, 선영이는 다음과 같이 고를 수 있다.

# 1 2 4 8
# 1 2 4 9
# 1 2 4 10
# 1 2 5 10

# 따라서 선영이는 로또를 4개 산다.
# 선영이는 돈이 엄청나게 많기 때문에, 수를 고르는 방법의 수 만큼 로또를 구매하며, 같은 방법으로 2장이상 구매하지 않는다.
# n과 m이 주어졌을 때, 선영이가 구매하는 로또의 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 n과 m으로 이루어져 있다.
# 각 테스트 케이스에 대해 선영이가 로또를 몇 개나 구매하는지 한 줄에 하나씩 출력한다.

# 제한
# 1 ≤ n ≤ 10
# 1 ≤ m ≤ 2,000
# n ≤ m

# https://kwoncorin.tistory.com/82

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    dp = [[0] * 2001 for _ in range(11)]
    dp[0] = [1] * 2001

    for index in range(1, 11):
        for num in range(1, 2001):
            dp[index][num] = dp[index][num - 1] + dp[index - 1][num // 2]

    test_case_count = int(readline())
    for _ in range(test_case_count):
        number_count, max_number = map(int, readline().split())
        print(dp[number_count][max_number])


solution()

# 4

# 1
# 4 10
