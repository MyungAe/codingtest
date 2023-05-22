import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    def change(index):
        if switch[index]:
            switch[index] = 0
        else:
            switch[index] = 1

    switch_count = int(readline())
    switch = [-1] + list(map(int, readline().split()))
    students = int(readline())

    for _ in range(students):
        sex, num = map(int, input().split())
        # 남자
        if sex == 1:
            for i in range(num, switch_count + 1, num):
                change(i)
        # 여자
        else:
            change(num)
            for k in range(switch_count // 2):
                if num + k > switch_count or num - k < 1:
                    break
                if switch[num + k] == switch[num - k]:
                    change(num + k)
                    change(num - k)
                else:
                    break

    for i in range(1, switch_count + 1):
        print(switch[i], end=" ")
        if i % 20 == 0:
            print()


solution()

# 1 0 0 0 1 1 0 1

# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3
