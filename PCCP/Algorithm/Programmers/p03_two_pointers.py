def solution(gems):
    # step 1. 자료형 생성

    # 1-1. 보석 종류 dict 생성 : 중복 제거
    unique_gems_dict = {gems : 0 for gems in set(gems)}
    # print(unique_gems_dict)

    # 1-2. 앞, 뒤 포인터 생성
    start, end = [0, 0]
    # print(start, end)

    # 1-3. 최소로 모두 구매할 보석의 개수 저장 변수 생성
    min_pointer_list = [-1, -1]
    min_gem = len(gems) + 1

    # step 2. for + while 순회

    # 2-1. dict 업데이트 함수 생성
    def update_dict(current_gems, pointer):
        if is_add(pointer):
            unique_gems_dict[current_gems] += 1
            return
        unique_gems_dict[current_gems] -= 1

    # 2-1-1. 보석을 제거해야 하는지, 추가해야 하는지 판별하는 함수
    def is_add(pointer):
        if pointer == 'end':
            return True
        return False

    # 2-2. 보석의 총 개수를 반환하는 함수
    def get_gem_count():
        return sum(list(unique_gems_dict.values()))

    # 2-3. 다 샀는지 판별하는 함수 생성
    def is_buy_all_jewel():
        if 0 not in list(unique_gems_dict.values()):
            return True
        return False

    # 2-4. 기존 개수와 비교하는 함수 생성
    def is_smaller(current_gems):
        nonlocal min_gem
        if min_gem > current_gems:
            return True
        return False

    # 2-5. start, end, min_jewel 업데이트 함수 생성
    def update_pointer(min_start, min_end, input_gems):
        nonlocal min_gem, min_pointer_list
        min_pointer_list = [min_start + 1, min_end + 1]
        min_gem = input_gems

    # 로직
    # for문 end로 순회
    for end in range(len(gems)):
        # 구매한 보석 dict를 업데이트
        update_dict(gems[end], 'end')
        # 만약 다 샀는데 && 기존 개수보다 적게 구매했다면
        current_gem_count = get_gem_count()
        if is_buy_all_jewel() and is_smaller(current_gem_count):
            # start, end, min_jewel 업데이트
            update_pointer(start, end, current_gem_count)
        # while 모든 보석을 샀다면:
        while is_buy_all_jewel():
            # start 앞으로 이동
            start += 1
            # 구매한 보석 dict를 업데이트 : 이전 보석
            update_dict(gems[start - 1], 'start')
            # 만약 다 샀는데 && 기존 개수보다 적게 구매했다면
            current_gem_count = get_gem_count()
            if is_buy_all_jewel() and is_smaller(current_gem_count):
                # start, end, min_jewel 업데이트
                update_pointer(start, end, current_gem_count)

    # step 3. 답 반환
    return min_pointer_list


# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))