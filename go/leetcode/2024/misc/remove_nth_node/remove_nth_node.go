package remove_nth_node

// https://leetcode.com/problems/remove-nth-node-from-end-of-list

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) ToSlice() []int {
	vals, cur := []int{}, l
	for cur != nil {
		vals = append(vals, cur.Val)
		cur = cur.Next
	}
	return vals
}

func NewList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := ListNode{}
	cur := &head
	for i, val := range vals {
		cur.Val = val
		if i < len(vals) - 1 {
			cur.Next = &ListNode{}
			cur = cur.Next
		}
	}
	return &head
}

// This was my first solution - O(n) but requires two passes over the list. It
// can be solved in a single pass.
func removeNthFromEndTwoPasses(head *ListNode, n int) *ListNode {
	if head == nil {
		return nil
	}
	length, cur := 0, head
	for cur != nil {
		cur = cur.Next
		length += 1
	}
	cur = head
	var left *ListNode
	for i := 0; i < length-n; i++ {
		left = cur
		cur = cur.Next
	}
	if left != nil {
		left.Next = cur.Next
		cur.Next = nil
		return head
	}
	return cur.Next
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if head == nil {
		return nil
	}
	dummy := ListNode{Next: head}
	left, right := &dummy, head
	for i := 0; i < n; i++ {
		right = right.Next
	}
	for right != nil {
		left, right = left.Next, right.Next
	}
	left.Next = left.Next.Next
	return dummy.Next
}
