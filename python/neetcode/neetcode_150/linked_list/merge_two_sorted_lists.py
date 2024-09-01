# https://neetcode.io/problems/merge-two-sorted-linked-lists
# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted linked list and return the head of the new
# sorted linked list.
#
# The new list should be made up of nodes from list1 and list2.
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]
#
# Example 2:
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]
#
# Example 3:
# Input: list1 = [], list2 = []
# Output: []
#
# Constraints:
#
# 0 <= The length of each list <= 100.
# -100 <= Node.val <= 100

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_str(self):
        s = f"{self.val}"
        head = self.next
        while head is not None:
            s += f", {head.val}"
            head = head.next
        return s


def merge(l1: ListNode, l2: ListNode):
    # Start a new list and add nodes to it.
    head = ListNode()
    tail = head
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l2 is not None:
        tail.next = l2
    elif l1 is not None:
        tail.next = l1
    return head.next


def test1():
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(1, ListNode(2, ListNode(3)))
    m = merge(l1, l2)
    assert m.to_str() == "1, 1, 2, 2, 3, 3"
