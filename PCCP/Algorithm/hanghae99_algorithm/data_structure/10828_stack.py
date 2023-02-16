"""
Q. 정수를 저장하는 스택을 구현
    push X: 정수 X를 스택에 넣는 연산이다.
    pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 스택에 들어있는 정수의 개수를 출력한다.
    empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

A. Correct : 32276kb 88ms
"""

import sys


def solution():
    # step 1. read input and make list
    repeat_count = int(sys.stdin.readline())
    orders = [sys.stdin.readline() for _ in range(repeat_count)]

    stack = [] * repeat_count

    # step 2. write methods
    def push(element):
        nonlocal stack
        stack += [element]
        return stack

    def pop():
        nonlocal stack
        stack_size = get_size()
        if stack_size:
            last_element = stack[stack_size - 1]
            stack = [stack[index] for index in range(len(stack) - 1)]
            print(last_element)
            return
        print('-1')

    def size():
        print(len(stack))

    def empty():
        if not get_size():
            print('1')
            return
        print('0')

    def top():
        if get_size():
            target = stack[len(stack) - 1]
            print(target)
            return target
        print('-1')

    def get_size():
        return len(stack)

    # step 3. do work
    for order in orders:
        if 'push' in order:
            method, num = order.split()
            push(num)
        if 'pop' in order:
            pop()
        if 'size' in order:
            size()
        if 'empty' in order:
            empty()
        if 'top' in order:
            top()

# Debugging
# 1. check input data
    # print(repeat_count, type(repeat_count))
    # print(order, type(order))
# 2. is funcs working ?
    # print(push(3))
    # print(pop())
    # print(size())
    # print(empty())
    # print(top())


solution()

# ex 1
'''
# input
14
push 1
push 2
top
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
top
'''

'''
# Output
2
2
0
2
1
-1
0
1
-1
0
3
'''

# ex 2
'''
# Input
7
pop
top
push 123
top
pop
top
pop
'''

'''
# Output
-1
-1
123
123
-1
-1
'''
