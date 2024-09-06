package stack

// https://neetcode.io/problems/minimum-stack
// https://leetcode.com/problems/min-stack/description/
// Minimum Stack
// Design a stack class that supports the push, pop, top, and getMin operations.
//
// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// Each function should run in O(1) time.
//
// Example 1:
// Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
// Output: [null,null,null,null,0,null,2,1]
//
// Explanation:
// MinStack minStack = new MinStack()
// minStack.push(1)
// minStack.push(2)
// minStack.push(0)
// minStack.getMin() // return 0
// minStack.pop()
// minStack.top()    // return 2
// minStack.getMin() // return 1
// Constraints:
//
// -2^31 <= val <= 2^31 - 1.
// pop, top and getMin will always be called on non-empty stacks.

type elem struct {
	val, min int
}

type MinStack struct {
	elems []elem
}

func Constructor() MinStack {
	return MinStack{}
}

func (s *MinStack) Push(val int) {
	m := val
	if len(s.elems) > 0 {
		m = min(m, s.GetMin())
	}
	s.elems = append(s.elems, elem{val: val, min: m})
}

func (s *MinStack) Pop() {
	s.elems = s.elems[:len(s.elems)-1]
}

func (s *MinStack) Top() int {
	return s.elems[len(s.elems)-1].val
}

func (s *MinStack) GetMin() int {
	return s.elems[len(s.elems)-1].min
}
