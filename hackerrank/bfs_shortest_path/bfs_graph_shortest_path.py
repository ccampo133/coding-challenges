# https://www.hackerrank.com/challenges/linkedin-practice-graph-theory-bfs/problem?h_r=internal-search
import queue
from typing import List, Dict

EDGE_LENGTH = 6


class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
        self.parent = None
        self.depth = None


def init_graph(num_nodes: int) -> Dict[int, Node]:
    graph = {}
    for i in range(1, num_nodes + 1):
        graph[i] = Node(i)
    return graph


def add_edge(graph: Dict[int, Node], n1: int, n2: int):
    node1, node2 = graph[n1], graph[n2]
    node1.children.append(node2)
    node2.children.append(node1)


def path_length(node: Node, depth: int = 0):
    if node.parent is None:
        return depth * EDGE_LENGTH
    return path_length(node.parent, depth + 1)


def bfs(graph: Dict[int, Node], start: int, end: int) -> int:
    visited, next_queue = set(), queue.Queue()
    visited.add(start)
    next_queue.put((graph[start], 1))
    while not next_queue.empty():
        node, depth = next_queue.get()
        if node.val == end:
            return (depth - 1) * EDGE_LENGTH
        for adjacent in node.children:
            if adjacent.val not in visited:
                visited.add(adjacent.val)
                next_queue.put((adjacent, depth + 1))
                adjacent.parent = node
    return -1


def bfs_total(graph: Dict[int, Node], start: int):
    visited, next_queue, node = set(), queue.Queue(), graph[start]
    visited.add(node.val)
    node.depth = 0
    next_queue.put(node)
    while not next_queue.empty():
        node = next_queue.get()
        for adjacent in node.children:
            if adjacent.val not in visited:
                adjacent.depth = node.depth + 1
                visited.add(adjacent.val)
                next_queue.put(adjacent)


def read_from_file(input_fname: str):
    with open(input_fname) as f:
        q = int(f.readline().rstrip('\n'))
        graphs, starts = [], []
        for i in range(q):
            n_nodes, n_edges = map(int, f.readline().rstrip('\n').split())
            graph = init_graph(n_nodes)
            for j in range(n_edges):
                n1, n2 = map(int, f.readline().rstrip('\n').split())
                add_edge(graph, n1, n2)
            graphs.append(graph)
            starts.append(int(f.readline().rstrip('\n')))
    return graphs, starts


def read_from_cli():
    q = int(input())
    graphs, starts = [], []
    for i in range(q):
        n_nodes, n_edges = map(int, input().split())
        graph = init_graph(n_nodes)
        for j in range(n_edges):
            n1, n2 = map(int, input().split())
            add_edge(graph, n1, n2)
        graphs.append(graph)
        starts.append(int(input()))
    return graphs, starts


if __name__ == '__main__':
    should_read_from_file = False

    if should_read_from_file:
        graphs, starts = read_from_file('testcase.txt')
        with open('expected_results.txt') as f:
            expected_results_lines = [line.rstrip() for line in f]
    else:
        graphs, starts = read_from_cli()

    for i in range(len(graphs)):
        graph = graphs[i]
        bfs_total(graph, starts[i])
        result = ''
        for n in graph:
            if n != starts[i]:
                node = graph[n]
                depth = node.depth * EDGE_LENGTH if node.depth is not None else -1
                result += str(depth) + ' '
        print(result)
        if should_read_from_file:
            assert expected_results_lines[i] == result.rstrip()

    # graph1 = init_graph(10)
    # add_edge(graph1, 1, 2)
    # add_edge(graph1, 1, 3)
    # add_edge(graph1, 3, 2)
    # add_edge(graph1, 4, 5)
    # add_edge(graph1, 4, 2)
    # add_edge(graph1, 9, 1)
    # add_edge(graph1, 6, 5)
    # add_edge(graph1, 9, 8)
    # add_edge(graph1, 7, 6)
    # add_edge(graph1, 8, 3)
    #
    # start = 1
    # res = bfs(graph1, start, 7)
    # print(res)
