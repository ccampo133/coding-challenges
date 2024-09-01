# https://neetcode.io/problems/linked-list-cycle-detection
# Linked List Cycle Detection
# Given the beginning of a linked list head, return true if there is a cycle in
# the linked list. Otherwise, return false.
#
# There is a cycle in a linked list if at least one node in the list that can be
# visited again by following the next pointer.
#
# Internally, index determines the index of the beginning of the cycle, if it
# exists. The tail node of the list will set it's next pointer to the index-th
# node. If index = -1, then the tail node points to null and no cycle exists.
#
# Note: index is not given to you as a parameter.
#
# Example 1:
# Input: head = [1,2,3,4], index = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# sthe 1st node (0-indexed).
#
# Example 2:
# Input: head = [1,2], index = -1
# Output: false
#
# Constraints:
#
# 1 <= Length of the list <= 1000.
# -1000 <= Node.val <= 1000
# index is -1 or a valid index in the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# This is the O(N) time and space solution. The other O(N)/O(1) solution
# requires knowledge of Floyd's tortoise and hare algorithm...
def cycle(l: ListNode) -> bool:
    s = set()
    while l is not None:
        if l in s:
            return True
        s.add(l)
        l = l.next
    return False


def cycle_floyd(l: ListNode) -> bool:
    slow, fast = l, l
    while fast is not None:
        fast = fast.next
        if fast is None:
            return False
        if fast == slow:
            return True
        fast = fast.next
        slow = slow.next
    return False
