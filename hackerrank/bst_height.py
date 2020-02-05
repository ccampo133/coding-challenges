# https://www.hackerrank.com/challenges/30-binary-search-trees/problem
# Get the height of a binary search tree.
# NOTE: the code is structured this way because it was mandated by HR.
# I wouldn't write in this styel normally.

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data <= root.data:
            cur = self.insert(root.left, data)
            root.left = cur
        else:
            cur = self.insert(root.right, data)
            root.right = cur
        return root

    def getHeight(self, root):
        if self.is_leaf(root):
            return 0
        left, right = 0, 0
        if root.left is not None:
            left += self.getHeight(root.left) + 1
        if root.right is not None:
            right += self.getHeight(root.right) + 1
        return max(left, right)

    def is_leaf(self, node):
        return node.left is None and node.right is None


if __name__ == '__main__':
    data = [3, 5, 2, 1, 4, 6, 7]
    myTree = Solution()
    root = None
    for i in data:
        root = myTree.insert(root, i)
    height = myTree.getHeight(root)
    assert height == 3
