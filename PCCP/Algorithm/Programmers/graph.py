# graph.py

# Graph
# graph를 그리는 종류 : 인접 리스트(간선 개수 기준, 공간 win) vs 인접 행렬(정점 개수 기준, 시간 win)

# 인접 그래프
graph = [
    [],
    [2, 3],
    [1, 3, 5],
    [1, 2, 5, 4],
    [3],
    [2, 3]
]

# BFS, DFS
# 나머자, 끝을 본다 = 가중치O : DFS + stack
# 최단거리 탐색 = 가중치 X : BFS + queue

# 리스트에서 뒤에 있는 원소를 빼면 DFS, pop()
# 앞에 있는 원소를 빼면 BFS, pop(0)


def dfs():
    start = 1
    vertex = 5
    # 목적지
    to_visits = [start]
    # 방문 체크
    is_visit = [False for _ in range(vertex + 1)]

    while to_visits:
        # 리스트 뒤의 값을 빼서 방문함
        now_visit = to_visits.pop()
        # 현재 위치 방문 여부 체크
        if not is_visit[now_visit]:
            # 방문 체크
            is_visit[now_visit] = True
            print(now_visit)
            # 목적지 추가
            to_visits += graph[now_visit]


def bfs():
    start = 1
    vertex = 5
    # 목적지
    to_visits = [start]
    # 방문 체크
    is_visit = [False for _ in range(vertex + 1)]

    while to_visits:
        # 리스트 뒤의 값을 빼서 방문함
        now_visit = to_visits.pop(0)
        # 현재 위치 방문 여부 체크
        if not is_visit[now_visit]:
            # 방문 체크
            is_visit[now_visit] = True
            print(now_visit)
            # 목적지 추가
            to_visits += graph[now_visit]


dfs()
# bfs()

s = 1
v = 5
visited = [False for _ in range(v + 1)]


def dfs_r(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            print(nxt)
            dfs_r(nxt)


dfs_r(s)
