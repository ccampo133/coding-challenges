# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        cur, prev = head.next, head
        while cur is not None:
            if cur.data == prev.data:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    mylist = Solution()
    inputs = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    head = None
    for data in inputs:
        head = mylist.insert(head, data)
    head = mylist.removeDuplicates(head)
    mylist.display(head)
