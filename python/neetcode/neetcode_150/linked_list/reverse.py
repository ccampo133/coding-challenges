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


def reverse(head: ListNode):
    head, tail = reverse_recur(head)
    head.next = None
    return tail


def reverse_recur(head: ListNode):
    if head.next is None:
        return (head, head)
    newhead, tail = reverse_recur(head.next)
    newhead.next = head
    return (head, tail)


def reverse_iter(head: ListNode):
    if head is None:
        return None
    if head.next is None:
        return None
    prev, cur = head, head.next
    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    head.next = None
    return prev


def test1():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    assert reverse(head).to_str() == "3, 2, 1, 0"


def test1_iter():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    assert reverse_iter(head).to_str() == "3, 2, 1, 0"
