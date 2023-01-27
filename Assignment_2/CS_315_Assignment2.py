class Node:

    def __init__(self, name):
        self.name = name
        self.adj = []


class Edge:

    def __init__(self, node1, node2, len):
        self.node1 = node1
        self.node2 = node2
        self.len = len


class Graph:

    def __init__(self, edges, nodes):
        self.edges = []
        self.nodes = []


def main():
    file_input = input("Enter a file: ")
    file = open(file_input, 'r')

    first_line = file.readline().split()

    nodes_amt = first_line[0]
    edges_amt = first_line[1]
    nodes = []
    edges = []

    for i in range(int(edges_amt)):
        line = file.readline().split()
        node1 = Node(line[0])
        node2 = Node(line[1])
        edge = Edge(node1, node2, line[2])
        #for i in nodes:
        #    if i.name !=
        #    nodes.append(node1)
        #if node2 not in nodes:
        #    nodes.append(node2)
        for i in nodes:
            if i.name == node1.name:
                break


        if edge not in edges:
            edges.append(edge)

    file.close()
    for i in nodes:
        print(i.name)
    for i in edges:
        print(i.node1.name, i.node2.name, i.len)

main()
