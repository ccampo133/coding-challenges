package add_two_ll

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

func FromSlice(vals []int) *ListNode {
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

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	carry := 0
	for l1 != nil || l2 != nil || carry > 0 {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		carry = sum / 10
		sum = sum % 10
		cur.Next = &ListNode{Val: sum}
		cur = cur.Next
	}
	return dummy.Next
}
