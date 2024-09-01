# https://neetcode.io/problems/binary-tree-diameter
# Binary Tree Diameter
# The diameter of a binary tree is defined as the length of the longest path
# between any two nodes within the tree. The path does not necessarily have to
# pass through the root.
#
# The length of a path between two nodes in a binary tree is the number of edges
# between the nodes.
#
# Given the root of a binary tree root, return the diameter of the tree.
#
# Example 1:
# Input: root = [1,null,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].
#
# Example 2:
# Input: root = [1,2,3]
# Output: 2
# Constraints:
#
# 1 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(node: TreeNode):
    max_dia = 0

    def dfs(node: TreeNode):
        if node is None:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        dia = l + r
        nonlocal max_dia
        if dia > max_dia:
            max_dia = dia
        return 1 + max(l, r)

    dfs(node)
    return max_dia


def test1():
    tree = TreeNode(1, right=TreeNode(2, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(4)))
    assert diameter(tree) == 3
