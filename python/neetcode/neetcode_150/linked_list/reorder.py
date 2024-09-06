# https://neetcode.io/problems/reorder-linked-list
# https://leetcode.com/problems/reorder-list/description/
# Reorder Linked List
# You are given the head of a singly linked-list.
#
# The positions of a linked list of length = 7 for example, can initially be
# represented as:
#
# [0, 1, 2, 3, 4, 5, 6]
#
# Reorder the nodes of the linked list to be in the following order:
#
# [0, 6, 1, 5, 2, 4, 3]
#
# Notice that in the general case for a list of length = n the nodes are
# reordered to be in the following order:
#
# [0, n-1, 1, n-2, 2, n-3, ...]
#
# You may not modify the values in the list's nodes, but instead you must
# reorder the nodes themselves.
#
# Example 1:
# Input: head = [2,4,6,8]
# Output: [2,8,4,6]
#
# Example 2:
# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]
#
# Constraints:
#
# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        l = []
        n = self
        while n is not None:
            l.append(n.val)
            n = n.next
        return l


def reorder(head: ListNode):
    stack = []
    node = head.next
    while node is not None:
        stack.append(node)
        node = node.next

    front = head
    num = len(stack) + 1
    for i in range(num):
        if (i + 1) % 2 == 0:
            n = stack.pop()
            n.next = front.next
            front.next = n
            front = n.next
    if num % 2 == 0:
        front.next.next = None
    else:
        front.next = None
    return


def test1():
    # [2, 4, 6, 8]
    l = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    reorder(l)
    assert l.to_list() == [2, 8, 4, 6]


def test2():
    # [0, 1, 2, 3, 4, 5, 6]
    l = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    reorder(l)
    assert l.to_list() == [0, 6, 1, 5, 2, 4, 3]
