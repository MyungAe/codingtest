import sys


def readline():
    return sys.stdin.readline()


bulb_count, command_count = map(int, readline().split())
bulbs = [0] + list(map(int, readline().split()))

for _ in range(command_count):
    command_type, b, c = map(int, readline().split())
    if command_type == 1:
        bulbs[b] = c

    elif command_type == 2:  # 전구 상태 변경
        for i in range(b, c + 1):
            if bulbs[i] == 0:
                bulbs[i] = 1
            elif bulbs[i] == 1:
                bulbs[i] = 0

    elif command_type == 3:  # 켜진 전구 끄기
        for i in range(b, c + 1):
            if bulbs[i] == 1:
                bulbs[i] = 0

    elif command_type == 4:  # 꺼진 전구 켜기
        for i in range(b, c + 1):
            if bulbs[i] == 0:
                bulbs[i] = 1

for i in range(1, bulb_count + 1):
    print(bulbs[i], end=' ')

