# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if not self.next:
            return str(self.val)
        return f'{self.val}->{self.next}'


# TODO: This one took a while... come back and take another look
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    soln = Solution()
    l1n1 = ListNode(1)
    l1n2 = ListNode(2)
    l1n3 = ListNode(4)
    l1n2.next = l1n3
    l1n1.next = l1n2

    l2n1 = ListNode(1)
    l2n2 = ListNode(3)
    l2n3 = ListNode(4)
    l2n2.next = l2n3
    l2n1.next = l2n2

    answer = soln.mergeTwoLists(l1n1, l2n1)
    print(answer)
