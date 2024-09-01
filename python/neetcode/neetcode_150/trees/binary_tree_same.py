# https://neetcode.io/problems/same-binary-tree
# Same Binary Tree
# Given the roots of two binary trees p and q, return true if the trees are
# equivalent, otherwise return false.
#
# Two binary trees are considered equivalent if they share the exact same
# structure and the nodes have the same values.
#
# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
# Example 2:
# Input: p = [4,7], q = [4,null,7]
# Output: false
#
# Example 3:
# Input: p = [1,2,3], q = [1,3,2]
# Output: false
#
# Constraints:
#
# 0 <= The number of nodes in both trees <= 100.
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def same_recur(p: TreeNode, q: TreeNode) -> bool:
    # Both trees are null - trivially the same.
    if p is None and q is None:
        return True
    # One tree is null - trivially different.
    if p is None or q is None:
        return False
    # Trees are not null and have different values.
    if p.val != q.val:
        return False
    # Now do it again for the subtrees.
    return same_recur(p.left, q.left) and same_recur(p.right, q.right)
