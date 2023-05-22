# 어떤 수열을 읽고, 홀수번째 수를 읽을 때 마다, 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.
# 예를 들어, 수열이 1, 5, 4, 3, 2 이면, 홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고, 1번째 수를 읽었을 때 중앙값은 1, 3번째 수를 읽었을 때는 4, 5번째 수를 읽었을 때는 3이다.
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)이 주어지고,
# 그 다음 줄부터 이 수열의 원소가 차례대로 주어진다. 원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수이다.
# 각 테스트 케이스에 대해 첫째 줄에 출력하는 중앙값의 개수를 출력하고, 둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력한다.
# 이때, 한 줄에 10개씩 출력해야 한다.
import sys
import heapq


def solution():
    # step 1. get input
    repeat_count = int(sys.stdin.readline().rstrip())

    for _ in range(repeat_count):
        input_data_count = int(sys.stdin.readline().rstrip())
        list_length = 0

        smaller_heap = []
        bigger_heap = []
        middle_value_list = []

        while list_length < input_data_count:
            data_list = list(map(int, sys.stdin.readline().rstrip().split()))
            for index, element in enumerate(data_list):
                # push elements
                if len(smaller_heap) == len(bigger_heap):
                    heapq.heappush(smaller_heap, -element)
                else:
                    heapq.heappush(bigger_heap, element)

                # compare and swap elements
                if bigger_heap and -smaller_heap[0] > bigger_heap[0]:
                    bigger_element = heapq.heappop(smaller_heap)
                    smaller_element = heapq.heappop(bigger_heap)
                    heapq.heappush(smaller_heap, -smaller_element)
                    heapq.heappush(bigger_heap, -bigger_element)

                # add middle element
                if not index % 2:
                    middle_value_list.append(-smaller_heap[0])

                list_length += 1

        answer_list_length = len(middle_value_list)
        count = 0
        print(answer_list_length)
        while count < answer_list_length:
            if count + 10 < answer_list_length:
                count += 10
                print(' '.join(map(str, middle_value_list[count - 10:count])))
            else:
                count += answer_list_length % 10
                print(' '.join(map(str, middle_value_list[count - answer_list_length % 10:count])))


solution()

# 5
# 1 2 3 4 5
# 5
# 9 8 7 6 5
# 12
# 23 23 22 22 13 3 5 5 3 -3
# -7 -3

# 3
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 9 8 7 6 5 4 3 2 1
# 23
# 23 41 13 22 -3 24 -31 -11 -8 -7
# 3 5 103 211 -311 -45 -67 -73 -81 -99
# -33 24 56
