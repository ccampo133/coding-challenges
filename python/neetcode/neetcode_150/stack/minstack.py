# https://neetcode.io/problems/minimum-stack
# https://leetcode.com/problems/min-stack/description/
# Minimum Stack
# Design a stack class that supports the push, pop, top, and getMin operations.
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.
#
# Example 1:
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
# Output: [null,null,null,null,0,null,2,1]
#
# Explanation:
# MinStack minStack = new MinStack()
# minStack.push(1)
# minStack.push(2)
# minStack.push(0)
# minStack.getMin() // return 0
# minStack.pop()
# minStack.top()    // return 2
# minStack.getMin() // return 1
# Constraints:
#
# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.

class Elem:
    def __init__(self, val: int, minimum: int):
        self.val = val
        self.minimum = minimum


class MinStack:

    def __init__(self):
        self.stack: list[Elem] = []

    def push(self, val: int) -> None:
        minimum = val
        if len(self.stack) > 0:
            minimum = min(self.getMin(), val)
        self.stack.append(Elem(val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].minimum


def test1():
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(0)
    assert stack.getMin() == 0
    stack.pop()
    assert stack.top() == 2
    assert stack.getMin() == 1
