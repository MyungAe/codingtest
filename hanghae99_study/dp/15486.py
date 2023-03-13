# 상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
# 백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

# N = 7인 경우에 다음과 같은 상담 일정표를 보자.
# 1일	2일	3일	4일	5일	6일	7일
# Ti	3	5	1	1	2	4	2
# Pi	10	20	10	20	15	40	200

# 1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.
# 상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다.
# 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

# 또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
# 퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
# 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N (1 ≤ N ≤ 1,500,000)이 주어진다.
# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 50, 1 ≤ Pi ≤ 1,000)
# 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
import sys


def readline():
    return sys.stdin.readline().strip()


def solution():
    days = int(readline())
    consult_times, consult_pays = [], []
    dp = [0 for _ in range(days + 1)]

    for _ in range(days):
        time, pay = map(int, readline().split())
        consult_times.append(time)
        consult_pays.append(pay)

    k = 0
    for index in range(days):
        k = max(k, dp[index])
        print(index, consult_times[index], k)
        complete_day = index + consult_times[index]
        if complete_day > days:
            continue
        print(consult_times[index], consult_pays[index])
        dp[complete_day] = max(k + consult_pays[index], dp[complete_day])
        print(dp)

    return max(dp)


print(solution())

# # step 1. get inputs
    # days = int(readline())
    # consult_requests = []
    #
    # for day in range(days):
    #     need_day, price = map(int, readline().split())
    #     # print(day, need_day, price)
    #
    #     consult_requests.append([need_day, price])
    #
    # # print(consult_requests)
    #
    # max_pay = 0
    #
    # for start_day in range(days):
    #     work_day = start_day
    #     final_pay = 0
    #     print('----')
    #     while days > work_day:
    #         print(work_day)
    #         consult_day = consult_requests[work_day][0]
    #         consult_pay = consult_requests[work_day][1]
    #         print(consult_day, consult_pay)
    #         if days >= work_day + consult_day:
    #             final_pay += consult_pay
    #         work_day += consult_day
    #         print(final_pay, work_day)
    #
    #     max_pay = max(max_pay, final_pay)
    #
    # return max_pay

# 45

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 55

# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10

# 20

# 10
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6

# 90

# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50
