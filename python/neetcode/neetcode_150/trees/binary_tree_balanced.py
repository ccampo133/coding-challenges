# https://neetcode.io/problems/balanced-binary-tree
# Balanced Binary Tree
# Given a binary tree, return true if it is height-balanced and false otherwise.
#
# A height-balanced binary tree is defined as a binary tree in which the left
# and right subtrees of every node differ in height by no more than 1.
#
# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: true
#
# Example 2:
# Input: root = [1,2,3,null,null,4,null,5]
# Output: false
#
# Example 3:
# Input: root = []
# Output: true
#
# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced(root: TreeNode) -> bool:
    # height returns the height of a binary tree if it is balanced. If the
    # tree is not balanced, it returns -1.
    def height(node: TreeNode):
        if node is None:
            return 0
        l = height(node.left)
        if l == -1:
            return -1
        r = height(node.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    return height(root) != -1


def test1():
    #      3
    #   /     \
    #  9      20
    #        / \
    #       15  7
    tree = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    assert balanced(tree)


def test2():
    #       1
    #      / \
    #     3   2
    #    /     \
    #   4       6
    #  /
    # 5
    tree = TreeNode(1, left=TreeNode(3, left=TreeNode(4, left=TreeNode(5))), right=TreeNode(2, right=TreeNode(6)))
    assert not balanced(tree)
