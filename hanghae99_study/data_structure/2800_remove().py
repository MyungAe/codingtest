# 어떤 수식이 주어졌을 때, 괄호를 제거해서 나올 수 있는 서로 다른 식의 개수를 계산하는 프로그램을 작성하시오.
# 이 수식은 괄호가 올바르게 쳐져 있다. 예를 들면, 1+2, (3+4), (3+4*(5+6))와 같은 식은 괄호가 서로 쌍이 맞으므로 올바른 식이다.
# 하지만, 1+(2*3, ((2+3)*4 와 같은 식은 쌍이 맞지 않는 괄호가 있으므로 올바른 식이 아니다.
# 괄호를 제거할 때는, 항상 쌍이 되는 괄호끼리 제거해야 한다.

# 예를들어 (2+(2*2)+2)에서 괄호를 제거하면, (2+2*2+2), 2+(2*2)+2, 2+2*2+2를 만들 수 있다.
# 하지만, (2+2*2)+2와 2+(2*2+2)는 만들 수 없다. 그 이유는 쌍이 되지 않는 괄호를 제거했기 때문이다.
# 어떤 식을 여러 쌍의 괄호가 감쌀 수 있다.

# 첫째 줄에 음이 아닌 정수로 이루어진 수식이 주어진다. 이 수식은 괄호가 올바르게 쳐져있다.
# 숫자, '+', '*', '-', '/', '(', ')'로만 이루어져 있다. 수식의 길이는 최대 200이고, 괄호 쌍은 적어도 1개, 많아야 10개이다.
from collections import deque


def solution():
    open_brackets = []  # stack
    close_brackets = deque()  # queue

    question_input = input()

    for index, element in enumerate(question_input):
        if element == '(':
            open_brackets.append(index)
        if element == ')':
            close_brackets.append(index)

    # 모든 경우의 수 구하기
    repeat_count = 2
    buckets_count = len(open_brackets)
    remove_buckets = [1]

    while repeat_count < buckets_count + 1:
        temp = []
        # print('연산 시작 전 기존 배열 : ', remove_buckets)
        # print('연산 시작')
        for element in remove_buckets:
            # print('연산 중인 요소 : ', element)
            # element가 int인 경우
            if isinstance(element, int):
                temp.append([element, repeat_count])
            # element가 list인 경우
            else:
                temp.append(sum([element], [repeat_count]))  # sum 확인하기
            # print('연산 값을 담은 배열 : ', temp)
        # print('기존 배열 : ', remove_buckets)
        remove_buckets = remove_buckets + [repeat_count] + temp
        # print('연산 후 배열 : ', remove_buckets)
        repeat_count += 1

    # print(sorted(remove_buckets, key=))

    result = []

    # 해당 인덱스의 괄호 제거
    for remove_index in remove_buckets:
        expression = list(question_input)  # << 문자열을 리스트로 바꿀 때, 2자리 이상의 숫자는 어떻게 될까?
        # print(remove_index)
        if isinstance(remove_index, int):
            open_bucket = open_brackets[remove_index - 1]
            close_bucket = close_brackets[-remove_index]
            expression[open_bucket] = ''
            expression[close_bucket] = ''
            # print(open_bucket, close_bucket)
        else:
            for index in remove_index:
                open_bucket = open_brackets[index - 1]
                close_bucket = close_brackets[-index]
                expression[open_bucket] = ''
                expression[close_bucket] = ''
                # print(open_bucket, close_bucket)
        # print(''.join(expression))
        result.append(''.join(expression))

    for element in sorted(set(result)):
        print(element)


solution()

# (0/0)
# 0/(0)
# 0/0

# (0/(0))

# (2+2*2+2)
# 2+(2*2)+2
# 2+2*2+2

# (2+(2*2)+2)

# (1+(2*3+4))
# (1+2*(3+4))
# (1+2*3+4)
# 1+(2*(3+4))
# 1+(2*3+4)
# 1+2*(3+4)
# 1+2*3+4

# (1+(2*(3+4)))

# (1+(2+3+(4+((5+6)+7)+8)+9+10
