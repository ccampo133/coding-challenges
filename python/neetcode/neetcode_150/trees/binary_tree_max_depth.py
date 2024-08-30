# https://neetcode.io/problems/depth-of-binary-tree
# Depth of Binary Tree
# Given the root of a binary tree, return its depth.
#
# The depth of a binary tree is defined as the number of nodes along the longest
# path from the root node down to the farthest leaf node.
#
# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: 3
#
# Example 2:
# Input: root = []
# Output: 0
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


def max_depth(node: TreeNode, depth=0):
    if node is None:
        return depth
    l = max_depth(node.left, depth + 1)
    r = max_depth(node.right, depth + 1)
    return max(l, r)


# iterative solution
def max_depth_iter(node: TreeNode):
    if node is None:
        return 0
    maxdepth = 0
    stack = [(node, 0)]
    while len(stack) > 0:
        node, depth = stack.pop()
        maxdepth = max(maxdepth, depth)
        if node is not None:
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))
    return maxdepth


def test1():
    root = TreeNode(
        val=1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
    )
    assert max_depth(root) == 3
    assert max_depth_iter(root) == 3
