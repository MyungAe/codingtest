# 포문 한 번에 2개의 포인터를 이용해 탐색 -> 시간복잡도 2n = n
# 뒤 포인터를 먼저 보내다 조건이 만족되면 앞 포인터가 순회
# 그러다 조건이 만족되지 않으면 뒤 포인터 순회 시작
# 이를 반복해 최적의 조건을 찾아야 한다

def solution(gems):
    answer = []
    return answer


# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))