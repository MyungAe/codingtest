# 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다.
# 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다.

# 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

import sys


def solution():
    # step 1. get repeat count(input)
    repeat_count = int(input())

    # step 2. repeat sth
    for _ in range(repeat_count):
        # step 2-1. get inputs
        doc_count, target_index = list(map(int, sys.stdin.readline().split()))
        queue = list(map(int, sys.stdin.readline().split()))
        max_value = max(queue)
        print_count = 0

        # step 3. calculate answer
        while True:
            # 가장 중요하지 않다면
            if queue[0] != max_value:
                # 제거해 큐에 다시 넣음
                element = queue.pop(0)
                queue.append(element)
                # 타겟 인덱스 변경
                target_index -= 1
                if target_index == -1:
                    target_index = len(queue) - 1
                continue

            # 가장 중요하다면
            if queue[0] == max_value:
                # 만약 타겟 인덱스 문서 차례이면
                if target_index == 0:
                    # 출력하고 반복문 종료
                    break
                # 아니라면 제거한 뒤 카운트 증가
                queue.pop(0)
                print_count += 1
                # 맥스값 재설정
                max_value = max(queue)
                # 타겟 인덱스 변경
                target_index -= 1
                if target_index == -1:
                    target_index = len(queue) - 1

        print(print_count + 1)

    # debuggers
    # print(doc_count, target_index)
    # print(queues)


solution()

# 1
# 2
# 5

# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1


# 1
# 1 0
# 5

# 1
# 4 2
# 1 2 3 4

# 1
# 6 0
# 1 1 9 1 1 1
