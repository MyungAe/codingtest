"""
Q. 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
    push X: 정수 X를 큐에 넣는 연산이다.
    pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 큐에 들어있는 정수의 개수를 출력한다.
    empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

    ++ 시간 제한 : 3초

A.
"""

import sys


def solution():
    # step 1. get input data
    repeat_count = int(sys.stdin.readline())
    queue = []
    queue_size = 0

    # step 2. write methods
    def push(num):
        nonlocal queue, queue_size
        queue = [num] + queue
        queue_size += 1

    def pop():
        nonlocal queue, queue_size
        if queue_size:
            front_element = queue[queue_size - 1]
            queue = queue[:queue_size - 1]
            print(front_element)
            queue_size -= 1
            return
        print('-1')

    def size():
        print(queue_size)

    def empty():
        if queue_size:
            print('0')
            return
        print('1')

    def front():
        if queue_size:
            print(queue[queue_size - 1])
            return
        print('-1')

    def back():
        if queue_size:
            print(queue[0])
            return
        print('-1')

    # step 3. do something
    # linked list or change cnt
    for count in range(repeat_count):
        order = sys.stdin.readline()
        if 'push' in order:
            _, number = order.split()
            push(number)
        if 'pop' in order:
            pop()
        if 'size' in order:
            size()
        if 'empty' in order:
            empty()
        if 'front' in order:
            front()
        if 'back' in order:
            back()

    # debugging
    # 1. show input data
        # print(repeat_count, orders)

    return


solution()

"""
# ex1
# Inputs
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""

"""
# Outputs
1
2
2
0
1
2
-1
0
1
-1
0
3
"""