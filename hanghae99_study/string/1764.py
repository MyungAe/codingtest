# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.
import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    not_listen, not_watch = map(int, readline().split())
    # print(not_listen, not_watch)

    # list in method time complexity : O(N)
    # set in method time complexity : O(1)

    # because set is hash table.
    # if hash table's load factor is too high, time complexity is O(n).
    # https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations

    not_listen_list = set()
    for index in range(not_listen):
        not_listen_list.add(readline())

    not_watch_list = set()
    for index in range(not_watch):
        not_watch_list.add(readline())

    count = 0
    all_person_list = []
    for person in not_watch_list:
        if person in not_listen_list:
            count += 1
            all_person_list.append(person)

    print(count)
    for person in sorted(all_person_list):
        print(person)


solution()

# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

# 2
# baesangwook
# ohhenrie
