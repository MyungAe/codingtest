def solution(input_string):
    answer = ''

    # 1. 중복 확인 dict + input_string list
    check_duplication = {element: 0 for element in set(input_string)}
    string_list = list(input_string)
    before_alphabet = ''

    # 2. string_list를 순회
    for alphabet in string_list:
        # 만약 이전 알파벳과 동일한 알파벳이라면
        if before_alphabet == alphabet:
            # 다음 순회
            continue
        # 아니라면
        else:
            # 만약 두 번째라면
            if check_duplication[alphabet] > 0:
                # 외톨이 알파벳이므로 정답에 추가
                answer += alphabet
            # 아니라면
            else:
                # 중복 확인 딕셔너리에 값 추가
                check_duplication[alphabet] += 1
        before_alphabet = alphabet

    # 3. 비어있으면 N으로 변환 / 값이 있다면 중복제거 + 정렬
    if not answer:
        return 'N'
    else:
        return ''.join(sorted(set(answer)))

# "de"
print(solution("edeaaabbccd"))

# "e"
print(solution("eeddee"))

# "N"
print(solution("string"))

# "bz"
print(solution("zbzbz"))