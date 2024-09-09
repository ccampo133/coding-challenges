# Remove Node From End of Linked List
# You are given the beginning of a linked list head, and an integer n.
#
# Remove the nth node from the end of the list and return the beginning of the list.
#
# Example 1:
# Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]
#
# Example 2:
# Input: head = [5], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 2
# Output: [2]
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(n: ListNode) -> list:
    l = []
    while n is not None:
        l.append(n.val)
        n = n.next
    return l


def remove_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left, right = dummy, head
    for i in range(n):
        right = right.next
    while right is not None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next


def test1():
    # [1, 2, 3, 4]
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    n = 2
    got = remove_from_end(l, n)
    assert to_list(got) == [1, 2, 4]


def test2():
    # [5]
    l = ListNode(5)
    n = 1
    got = remove_from_end(l, n)
    assert to_list(got) == []


def test3():
    # [1, 2]
    l = ListNode(1, ListNode(2))
    n = 2
    got = remove_from_end(l, n)
    assert to_list(got) == [2]


def test4():
    # [0, 1, 4, 5, 7, 6]
    l = ListNode(0, ListNode(1, ListNode(4, ListNode(5, ListNode(7, ListNode(6))))))
    n = 2
    got = remove_from_end(l, n)
    assert to_list(got) == [0, 1, 4, 5, 6]
