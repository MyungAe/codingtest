# 춘향이는 편의점 카운터에서 일한다.
# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다.
# 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.
# 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를,
# 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.
# 첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.
# 거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


# 로직
# 5로 나눈 나머지가 홀수 -> 5를 하나 줄여서 2로 나눈다
# 5로 나눈 나머지가 짝수 -> 2로 나눈다
# 5로 나누어지지 않는다 + 홀수이다 -> -1
def solution():
    unit_coins = [5, 2]
    answers = []
    counts = 0

    payment_amount = int(readline())

    for coin in unit_coins:
        counts += payment_amount // coin
        payment_amount = payment_amount % coin

        if counts and payment_amount % 2:
            counts -= 1
            payment_amount += coin

    if counts:
        answers.append(counts)

    if not answers:
        return -1

    return min(answers)


print(solution())

# 13

# 5

# 14

# 4
