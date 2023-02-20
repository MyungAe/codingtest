# 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다.
# (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다)
# 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다.
# 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.
# 후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

# 피연산자 조건 : 1 <= 개수 <= 26, 크기(자연수) <= 100
# 식 (중간)결과 조건 : -20억 <= 결과 <= 20억

# ! 후위 표기식 읽는 법
# Ex) ABC*+DE/-
# 1. B * C = 6
# 2. A + 6 = 7
# 3. D / E = 0.8
# 4. 7 - 0.8 = 6.2

# 풀이 방법 고민
# 문자열로 저장 : 실수 처리가 애매
# 스택으로 저장 (해결)

def solution():
    # step 1. get input
    operand_count = int(input())
    expression = input()
    operands = [int(input()) for _ in range(operand_count)]

    queue = []  # << stack, not queue

    def is_operator(char):
        if char == '+':
            return True
        if char == '-':
            return True
        if char == '*':
            return True
        if char == '/':
            return True
        return False

    def is_alphabet(char):
        if isinstance(char, str) and 64 < ord(char) < 91:
            return True
        return False

    def change_operand(operand1, operand2):
        if is_alphabet(operand1):
            operand1 = operands[ord(operand1) - 65]
        if is_alphabet(operand2):
            operand2 = operands[ord(operand2) - 65]
        # print('change_operand : ', operand1, operand2)
        return float(operand1), float(operand2)

    def calculate_expression(operand1, operand2, operator):
        operand1, operand2 = change_operand(operand1, operand2)
        # print('calculate expression', operand1, operand2, operator)
        if operator == '+':
            return operand1 + operand2
        if operator == '-':
            return operand1 - operand2
        if operator == '*':
            return operand1 * operand2
        if operator == '/':
            return operand1 / operand2

    # step 2. repeat calculating expression
    for string in expression:
        if not is_operator(string):
            queue.append(string)
            continue

        if is_operator(string):
            element1 = queue.pop()
            element2 = queue.pop()
            result = calculate_expression(element2, element1, string)
            queue.append(result)

    # step 3. return answer
    return f'{queue[0]:.2f}'

    # debugs
    # print(operand_count, expression, operands)
    # print(queue[length - 1], queue[length - 2], queue[length - 3])
    # print(result, queue)
    # print(answer)


print(solution())

# ex 1

# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# 6.20

# ex 2

# 1
# AA+A+
# 1

# 3.00
