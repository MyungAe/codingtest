# 로니 콜먼 동영상을 보고 보디빌더가 되기로 결심한 향빈이는 PT 상담을 받으러 서강헬스클럽에 갔다.
# 향빈이가 서강헬스클럽을 선택한 이유는 PT를 받을 때 사용하는 운동기구를 회원이 선택할 수 있다는 점 때문이다.
# 하지만, 서강헬스클럽은 항상 사람이 많아서 PT를 한 번 받을 때 운동기구를 최대 두 개까지만 선택할 수 있다.

# N개의 운동기구를 한 번씩 사용해보고 싶은 향빈이는 PT를 받을 때마다 이전에 사용하지 않았던 운동기구를 선택하기로 계획을 세웠다.
# 그리고 비용을 절약하기 위해 PT를 받을 때 운동기구를 되도록이면 두 개를 사용하기로 했다.
# 예를 들어, 헬스장에 총 10개의 운동기구가 있을 경우 PT를 5번 받으면 모든 기구를 다 사용할 수 있다.
# 9개의 운동기구가 있는 경우에도 PT를 5번 받지만, 마지막 PT를 받을 때는 운동기구를 하나만 사용한다.

# 하지만 향빈이는 운동기구를 선택하다가 큰 고민에 빠졌다. 왜냐하면 운동기구마다 근손실이 일어나는 정도가 다르기 때문이다.
# 어떤 운동기구는 자극이 잘 안 와서 근손실이 적게 일어나는데, 어떤 운동기구는 자극이 잘 와서 근손실이 많이 일어난다.
# 근손실이 죽음보다 무서운 향빈이는 PT를 한 번 받을 때의 근손실 정도가 M을 넘지 않도록 하고 싶다.
# 이때, M의 최솟값을 구해보자. 참고로, 운동기구를 두 개 사용해서 PT를 받을 때의 근손실 정도는 두 운동기구의 근손실 정도의 합이다.

# 첫째 줄에 서강헬스클럽에 비치된 운동기구의 개수를 나타내는 정수 N이 주어진다. (1 <= N <= 10000)
# 둘째 줄에는 각 운동기구의 근손실 정도를 나타내는 정수 t1, t2, ..., t_N가 주어진다. (0 <= ti <= 10^18)
# M의 최솟값을 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    # step1. sort input
    gym_equipment = int(readline())
    exercise_stresses = sorted(map(int, readline().split()))
    # print(gym_equipment, exercise_stresses)

    # step2. check size : is odd? or even
    add_stresses = []
    if gym_equipment % 2:
        add_stresses.append(exercise_stresses.pop())

    # step3. sum min and max, append value
    for index in range(gym_equipment // 2):
        add_stresses.append(exercise_stresses[index] + exercise_stresses[-index - 1])
    # print(add_stresses)

    # step4. return max value
    print(max(add_stresses))


solution()

# 5
# 1 2 3 4 5

# 5
