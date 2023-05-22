# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.
# 첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.
# 첫째 줄에 프리오더를 출력한다.
import sys
# sys.setrecursionlimit(10 ** 5)


def solution():
    # step 1. get inputs
    node_count = int(sys.stdin.readline())

    in_order = sys.stdin.readline().rstrip().split()
    post_order = sys.stdin.readline().rstrip().split()

    tree = ['0'] * (node_count + 1)

    def make_tree(inorder, index):
        nonlocal tree
        tree_length = len(inorder)

        # print(inorder, tree, len(tree), index)

        if tree_length > 2:
            middle_index = int(tree_length / 2)
            tree[index] = inorder[middle_index]

            if len(tree) > index * 2:
                left_tree = inorder[:middle_index]
                make_tree(left_tree, index * 2)

            if len(tree) > index * 2 + 1:
                right_tree = inorder[middle_index + 1:]
                make_tree(right_tree, index * 2 + 1)

        if tree_length < 3:
            if len(tree) > index:
                tree[index] = inorder[1]
                if len(tree) > index + 1 and len(inorder) > 1:
                    tree[index + 1] = inorder[0]

        print(tree)

    def preorder(node_index):
        nonlocal tree
        if node_index < len(tree):
            print(tree[node_index], end=' ')
            preorder(node_index * 2)
            preorder(node_index * 2 + 1)

    make_tree(in_order, 1)
    preorder(1)
    # print(tree)


solution()

# 2 1 3

# 3
# 1 2 3
# 1 3 2

# 3 2 1 4

# 4
# 1 2 3 4
# 1 2 4 3
