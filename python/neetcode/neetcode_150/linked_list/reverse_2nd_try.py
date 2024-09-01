# https://neetcode.io/problems/reverse-a-linked-list
# Reverse a Linked List
# Given the beginning of a singly linked list head, reverse the list, and return
# the new beginning of the list.
#
# Example 1:
#
# Input: head = [0,1,2,3]
#
# Output: [3,2,1,0]
# Example 2:
#
# Input: head = []
#
# Output: []
# Constraints:
#
# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_str(self):
        s = str(self.val)
        next = self.next
        while next is not None:
            s += f", {next.val}"
            next = next.next
        return s


def reverse(node):
    if node is None:
        return None
    prev, cur = node, node.next
    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    node.next = None
    return prev
