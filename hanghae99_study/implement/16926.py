# 크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.

# A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
#    ↓                                       ↑
# A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
#    ↓         ↓                   ↑         ↑
# A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
#    ↓                                       ↑
# A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]

# 예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.

# 1 2 3 4       2 3 4 8       3 4 8 6
# 5 6 7 8       1 7 7 6       2 7 8 2
# 9 8 7 6   →   5 6 8 2   →   1 7 6 3
# 5 4 3 2       9 5 4 3       5 9 5 4
#  <시작>         <회전1>        <회전2>

# 배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

# 첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.
# 둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.
# 입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    row, column, rotate = map(int, readline().split())
    array = []

    for _ in range(row):
        array.append(list(map(int, readline().split())))
    # print(array)

    for _ in range(rotate):
        for i in range(min(row, column) // 2):
            s_row, s_column = i, i
            s_value = array[s_row][s_column]

            for j in range(i + 1, row - i):  # 좌
                s_row = j
                prev_value = array[s_row][s_column]
                array[s_row][s_column] = s_value
                s_value = prev_value

            for j in range(i + 1, column - i):  # 하
                s_column = j
                prev_value = array[s_row][s_column]
                array[s_row][s_column] = s_value
                s_value = prev_value

            for j in range(i + 1, row - i):  # 우
                s_row = row - j - 1
                prev_value = array[s_row][s_column]
                array[s_row][s_column] = s_value
                s_value = prev_value

            for j in range(i + 1, column - i):  # 상
                s_column = column - j - 1
                prev_value = array[s_row][s_column]
                array[s_row][s_column] = s_value
                s_value = prev_value
    # print(array)

    for i in range(row):
        for j in range(column):
            print(array[i][j], end=' ')
        print()


solution()

# 3 4 8 12
# 2 11 10 16
# 1 7 6 15
# 5 9 13 14

# 4 4 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
