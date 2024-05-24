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


def bfs(start: Node):
    visited, next_queue = set(), queue.Queue()
    visited.add(start.val)
    start.depth = 0
    next_queue.put(start)
    while not next_queue.empty():
        node = next_queue.get()
        for adjacent in node.children:
            if adjacent.value not in visited:
                adjacent.depth = node.depth + 1
                visited.add(adjacent.value)
                next_queue.put(adjacent)


def read(input_func):
    q = int(input_func())
    graphs = []
    for i in range(q):
        n_nodes, n_edges = map(int, input_func().split())
        graph = init_graph(n_nodes)
        for j in range(n_edges):
            n1, n2 = map(int, input_func().split())
            add_edge(graph, n1, n2)
        start = int(input_func())
        graphs.append((graph, start))
    return graphs


def read_from_cli():
    return read(lambda: input())


def read_from_file(input_fname: str):
    with open(input_fname) as f:
        return read(lambda: f.readline().rstrip('\n'))


if __name__ == '__main__':
    should_read_from_file = True

    if should_read_from_file:
        graphs = read_from_file('testcase.txt')
        with open('expected_results.txt') as f:
            expected_results_lines = [line.rstrip() for line in f]
    else:
        graphs = read_from_cli()

    for i in range(len(graphs)):
        graph, start = graphs[i]
        bfs(graph[start])
        result = ''
        for n in graph:
            if n != start:
                node = graph[n]
                depth = node.depth * EDGE_LENGTH if node.depth is not None else -1
                result += str(depth) + ' '
        print(result)
        if should_read_from_file:
            assert expected_results_lines[i] == result.rstrip()
