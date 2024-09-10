package cp_linkedlist_rand

// https://leetcode.com/problems/copy-list-with-random-pointer/description/

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	nodes := make(map[*Node]*Node)
	cur := head
	for cur != nil {
		nodes[cur] = &Node{Val: cur.Val}
		cur = cur.Next
	}
	for oldNode, newNode := range nodes {
		newNode.Next = nodes[oldNode.Next]
		newNode.Random = nodes[oldNode.Random]
	}
	return nodes[head]
}
