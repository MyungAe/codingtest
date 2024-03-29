# 2개의 문자열 s와 t가 주어졌을 때 s가 t의 부분 문자열인지 판단하는 프로그램을 작성하라.
# 부분 문자열을 가지고 있는지 판단하는 방법은 t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우를 이야기 한다.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문자열 s 와 t가 빈칸을 사이에 두고 들어온다.
# s와 t의 길이는 10만을 넘지 않는다.
# 입력된 s와 t의 순서대로 s가 t의 부분 문자열인 경우 Yes라 출력하고 아닐 경우 No라고 출력한다.

import sys


def readline():
    return sys.stdin.readline().rstrip()


def solution():
    while True:
        input_data = readline()
        if input_data == '':
            break

        s, t = input_data.split()

        is_correct = False
        before_char_index = 0

        for char in t:
            if char == s[before_char_index]:
                before_char_index += 1
                if before_char_index == len(s):
                    is_correct = True
                    break

        if is_correct:
            print("Yes")
        else:
            print("No")


solution()

# sequence subsequence
# person compression
# VERDI vivaVittorioEmanueleReDiItalia
# caseDoesMatter CaseDoesMatter

# Yes
# No
# Yes
# No
