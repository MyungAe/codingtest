# 닭이 길을 건너간 이유는 과학적으로 깊게 연구가 되어 있지만, 의외로 소가 길을 건너간 이유는 거의 연구된 적이 없다.
# 이 주제에 관심을 가지고 있었던 농부 존은 한 대학으로부터 소가 길을 건너는 이유에 대한 연구 제의를 받게 되었다.
# 존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다. 존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다.
# 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.
# 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.

# 첫 줄에 관찰 횟수 N이 주어진다. N은 100 이하의 양의 정수이다. 다음 N줄에는 한 줄에 하나씩 관찰 결과가 주어진다. 관찰 결과는 소의 번호와 위치(0 또는 1)로 이루어져 있다.
# 첫 줄에 소가 길을 건너간 최소 횟수를 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    cows_count = int(readline())
    cows_snapshot = [-1] * 11
    answer = 0
    # print(cows_snapshot)

    for i in range(cows_count):
        cows_number, cows_current_location = map(int, readline().split())

        if cows_snapshot[cows_number] == -1:
            cows_snapshot[cows_number] = cows_current_location
            continue

        if cows_snapshot[cows_number] != cows_current_location:
            answer += 1
            cows_snapshot[cows_number] = cows_current_location

        # print(cows_snapshot)

    return answer


print(solution())

# 3

# 8
# 3 1
# 3 0
# 6 0
# 2 1
# 4 1
# 3 0
# 4 0
# 3 1
