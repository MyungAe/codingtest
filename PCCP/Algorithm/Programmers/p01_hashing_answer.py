def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    # 신고 내역
    history = {}
    # 신고 횟수
    report_count = {}

    # 초기화
    for user in id_list:
        # user 가 신고한 내역은 처음에 비어 있는 리스트
        history[user] = []
        # user 의 누적 신고 횟수는 0회
        report_count[user] = 0

    # report 를 순회하며, 신고내역/신고회수 저장
    for from_to in report:
        from_user, to_user = from_to.split()
        # 기존에 from_user 가 to_user를 신고한 적이 없다면,
        if to_user not in history[from_user]:
            history[from_user].append(to_user)
            report_count[to_user] += 1

    # idx와 요소(user이름)을 동시에 꺼내며
    for idx, user in enumerate(id_list):
        # user가 신고한 사람들을 순회하며
        for report_user in history[user]:
            # 신고당한 사람의 누적 횟수가 k보다 크면
            if report_count[report_user] >= k:
                # 신고한 사람이 받을 메일 개수 +1
                answer[idx] += 1
    return answer


# [2, 1, 1, 0]
print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
))

# [0, 0]
print(solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
))
