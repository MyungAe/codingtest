import sys
import heapq


def solution():
    # step 1. get repeat count in input
    repeat_count = int(sys.stdin.readline().rstrip())

    heap_queue = []
    for _ in range(repeat_count):
        data = sys.stdin.readline().rstrip().split()
        for element in data:
            heapq.heappush(heap_queue, int(element))
            if len(heap_queue) > repeat_count:
                heapq.heappop(heap_queue)

    # step 3. repeat is completed, print biggest one
    return heap_queue[0]


print(solution())
