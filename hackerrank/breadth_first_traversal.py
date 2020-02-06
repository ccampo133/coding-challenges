# https://www.hackerrank.com/challenges/30-binary-trees/problem


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data <= root.data:
            cur = self.insert(root.left, data)
            root.left = cur
        else:
            cur = self.insert(root.right, data)
            root.right = cur
        return root

    def levelOrder(self, root):
        visited = [root]
        output = ''
        while len(visited) > 0:
            node = visited.pop()
            output += str(node.data) + ' '

            if node.left is not None:
                visited.insert(0, node.left)

            if node.right is not None:
                visited.insert(0, node.right)
        print(output)


# Write your code here

if __name__ == '__main__':
    inputs = [3, 5, 4, 7, 2, 1]
    myTree = Solution()
    root = None
    for data in inputs:
        root = myTree.insert(root, data)
    myTree.levelOrder(root)
