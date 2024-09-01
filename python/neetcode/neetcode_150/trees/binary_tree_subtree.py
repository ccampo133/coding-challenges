# https://neetcode.io/problems/subtree-of-a-binary-tree
# https://leetcode.com/problems/subtree-of-another-tree/description/
# Subtree of a Binary Tree
# Given the roots of two binary trees `root` and `subRoot`, return true if there
# isa subtree of root with the same structure and node values of `subRoot` and
# false otherwise.
#
# A subtree of a binary tree `tree` is a tree that consists of a node in tree
# and all of this node's descendants. The tree `tree` could also be considered
# as a subtree of itself.
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
#
# Output: true
# Example 2:
#
#
#
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
#
# Output: false
# Constraints:
#
# 0 <= The number of nodes in both trees <= 100.
# -100 <= root.val, subRoot.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_sub(root: TreeNode, sub: TreeNode) -> bool:
    stack = [root]
    while len(stack) > 0:
        r = stack.pop()
        if same(r, sub):
            return True
        if r is not None:
            stack.append(r.right)
            stack.append(r.left)
    return False


# same returns true if two binary trees are the same.
def same(p: TreeNode, q: TreeNode) -> bool:
    s1, s2 = [p], [q]
    while len(s1) != 0 and len(s2) != 0:
        p, q = s1.pop(), s2.pop()
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            s1.append(p.right)
            s1.append(p.left)
            s2.append(q.right)
            s2.append(q.left)
    return True
