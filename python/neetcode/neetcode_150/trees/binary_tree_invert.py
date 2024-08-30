# https://neetcode.io/problems/invert-a-binary-tree
# Invert a Binary Tree
# You are given the root of a binary tree root. Invert the binary tree and
# return its root.
#
# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,3,2,7,6,5,4]
#
# Example 2:
# Input: root = [3,2,1]
# Output: [3,1,2]
#
# Example 3:
# Input: root = []
# Output: []
#
# Constraints:
#
# 0 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def invert(root: TreeNode):
    if root is None:
        return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invert(root.left)
    invert(root.right)
    return root


def test1():
    root = TreeNode(
        val=1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
    )
    invert(root)
    print(root)
