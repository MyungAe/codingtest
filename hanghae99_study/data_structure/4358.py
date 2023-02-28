# 생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.
# 프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어진다.
# 어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어진다.
# 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.
import sys


def solution():
    # step 1. get inputs
    tree_dicts = {}
    count = 0

    while True:
        input_data = sys.stdin.readline().rstrip()
        if not input_data:
            break
        if input_data not in tree_dicts:
            tree_dicts[input_data] = 0
        tree_dicts[input_data] += 1
        count += 1

    tree_list = list(tree_dicts.keys())
    tree_list.sort()

    for tree in tree_list:
        print(f'{tree} {tree_dicts[tree] / count * 100:.4f}')


solution()

# Ash 13.7931
# Aspen 3.4483
# Basswood 3.4483
# Beech 3.4483
# Black Walnut 3.4483
# Cherry 3.4483
# Cottonwood 3.4483
# Cypress 3.4483
# Gum 3.4483
# Hackberry 3.4483
# Hard Maple 3.4483
# Hickory 3.4483
# Pecan 3.4483
# Poplan 3.4483
# Red Alder 3.4483
# Red Elm 3.4483
# Red Oak 6.8966
# Sassafras 3.4483
# Soft Maple 3.4483
# Sycamore 3.4483
# White Oak 10.3448
# Willow 3.4483
# Yellow Birch 3.4483

# Red Alder
# Ash
# Aspen
# Basswood
# Ash
# Beech
# Yellow Birch
# Ash
# Cherry
# Cottonwood
# Ash
# Cypress
# Red Elm
# Gum
# Hackberry
# White Oak
# Hickory
# Pecan
# Hard Maple
# White Oak
# Soft Maple
# Red Oak
# Red Oak
# White Oak
# Poplan
# Sassafras
# Sycamore
# Black Walnut
# Willow
