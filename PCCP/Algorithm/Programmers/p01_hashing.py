def solution(id_list, report, k):
    # step1. make dict
    id_dict = {id : 0 for id in id_list}

    # step2. cal report count
    # 중복 방지 로직은 어떻게? 신고 내역 dict를 만들어서 중복을 알아내자
    for report_value in report:
        reporter, reported = report_value.split()
        if reported in id_dict:
            id_dict[reported] += 1

    # step3. find reporter
    id_suspend = []
    for key, value in id_dict.items():
        if value >= k:
            id_suspend.append(key)

    # step4. make answer dicts
    answer_dicts = {id : 0 for id in id_list}
    for report_value in report:
        reporter, reported = report_value.split()
        if reported in id_suspend:
            answer_dicts[reporter] += 1

    # step5. dict to list
    return list(answer_dicts.values())

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