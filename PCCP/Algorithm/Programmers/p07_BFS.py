# from collections import deque


def solution(start, end):
    answer = 0

    # 필요 자료구조
    to_visit = [start]
    # to_visit.append(deque)
    is_visited = [False for _ in range(10001)]

    # 순회
    while to_visit:
        for _ in range(len(to_visit)):
            now_visit = to_visit.pop(0)
            if now_visit == end:
                return answer
            if not is_visited[now_visit]:
                is_visited[now_visit] = True
                to_visit += [now_visit - 1, now_visit + 1, now_visit + 5]

        answer += 1


# 3
print(solution(5, 14))

# 5
print(solution(8, 3))