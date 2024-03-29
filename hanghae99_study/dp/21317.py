# 심마니 영재는 산삼을 찾아다닌다.
# 산삼을 찾던 영재는 N개의 돌이 일렬로 나열되어 있는 강가를 발견했고, 마지막 돌 틈 사이에 산삼이 있다는 사실을 알게 되었다.
# 마지막 돌 틈 사이에 있는 산삼을 캐기 위해 영재는 돌과 돌 사이를 점프하면서 이동하며 점프의 종류는 3가지가 있다.
# 점프의 종류에는 현재 위치에서 다음 돌로 이동하는 작은 점프, 1개의 돌을 건너뛰어 이동하는 큰 점프, 2개의 돌을 건너뛰어 이동하는 매우 큰 점프가 있다.
# 각 점프를 할 때는 에너지를 소비하는데, 이 때 작은 점프와 큰 점프시 소비되는 에너지는 점프를 하는 돌의 번호마다 다르다.
# 매우 큰 점프는 단 한 번의 기회가 주어지는데, 이때는 점프를 하는 돌의 번호와 상관없이 k만큼의 에너지를 소비한다.
# 에너지를 최대한 아껴야 하는 영재가 산삼을 얻기 위해 필요한 에너지의 최솟값을 구하여라.
# 영재는 첫 번째 돌에서부터 출발한다.

# 첫 번째 줄에는 돌의 개수 N이 주어진다.
# N - 1개의 줄에 걸쳐서, 1번 돌부터 N - 1번 돌 까지의 작은 점프를 하기 위해 필요한 에너지, 큰 점프를 하기 위해 필요한 에너지가 주어진다.
# 마지막 줄에는 K가 주어진다.
# 산삼을 얻기 위해 필요한 영재의 최소 에너지를 출력한다.

# 1 ≤ N ≤ 20
# 작은 점프, 큰 점프 시 필요한 에너지와 K는 5,000을 넘지않는 자연수이다.
import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    stone_count = int(readline())
    stone_energy = []

    dp = [1e9 for _ in range(stone_count)]
    dp[0] = 0

    for index in range(stone_count - 1):
        small_jump, big_jump = map(int, readline().split())
        stone_energy.append((small_jump, big_jump))
        if index + 1 < stone_count:
            dp[index + 1] = min(dp[index + 1], dp[index] + small_jump)
        if index + 2 < stone_count:
            dp[index + 2] = min(dp[index + 2], dp[index] + big_jump)
        print(stone_energy[index][0] == small_jump)
        print(stone_energy[index][1] == big_jump)

    # huge_jump_energy
    huge_jump = int(readline())

    _min = dp[-1]
    for i in range(3, stone_count):
        e, dp1, dp2 = dp[i - 3] + huge_jump, 1e9, 1e9
        for j in range(i, stone_count - 1):
            if i + 1 <= stone_count:
                dp1 = min(dp1, e + stone_energy[j][0])
            if i + 2 <= stone_count:
                dp2 = min(dp2, e + stone_energy[j][1])
            # print(e, dp1, dp2)
            e, dp1, dp2 = dp1, dp2, 1e9
        _min = min(_min, e)

    return _min


print(solution())

# 5

# 5
# 1 2
# 2 3
# 4 5
# 6 7
# 4

# 10
# 1 2
# 2 3
# 4 5
# 6 7
# 4 3
# 1 2
# 2 3
# 4 5
# 6 7
# 4


