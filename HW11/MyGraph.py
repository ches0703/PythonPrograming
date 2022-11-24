# MyGraph.py
# MyGraph.py - user-defined module for Graph data structure (1)
"""
Project : user-defined module for Graph data structure
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 24
Update list:
    - v1.1 : 11 / 24
        Make class Node, Edge, WeightedEdge, WeightedGraph
        Add Print method in WeightedGraph : printEdges(), printDistanceTable()
"""


# Node : Point with name
class Node:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


#  Edge : Save the inforaition of conneted between point
class Edge:
    def __init__(self, src_name, dest_name):
        self.src_name = src_name
        self.dest_name = dest_name

    def getSrcName(self):
        return self.src_name

    def getDestName(self):
        return self.dest_name

    def __str__(self):
        return "{} -> {}".format(self.src_name, self.dest_name)


# WeightedEdge : Edge data + Weight(distance of connected point)
class WeightedEdge(Edge):
    def __init__(self, src_name, dest_name, weight=1.0):
        super(WeightedEdge, self).__init__(
            src_name, dest_name)  # Super class init
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return "{:3}--({:4})->{:>3}".format(self.src_name, self.weight, self.dest_name)


# WeightedGraph : Graph with WeightedEdge & Node
class WeightedGraph:
    def __init__(self):
        self.nodes = []             # List of Node
        self.node_names = []        # List of Node's name
        self.adjacency_nodes = {}   # dict of {src_node : list of adjacency_node}
        self.weighted_edges = []    # List of WeightedEdge
        # dict of {edge(src_name, dest_name) : weight}
        self.edge_weights = {}

    # Add Node in List : nodes, node_names & inti adjacency_nodes
    def addNode(self, node: Node):
        if node.getName() not in self.node_names:     # Check Duplicate & Add Node
            self.nodes.append(node)
            self.node_names.append(node.getName())
            self.adjacency_nodes[node.getName()] = []

    # Add Edge in dict : add in adjacency_nodes's list, add in edgeweights
    def addEdge(self, weighted_edge: WeightedEdge):
        src_name = weighted_edge.getSrcName()
        dest_name = weighted_edge.getDestName()
        # Check Edge's element in node's list(nodes, node_names)
        if not ((src_name in self.node_names) and (dest_name in self.node_names)):
            raise ValueError("")
        self.weighted_edges.append(weighted_edge)
        # add in adjacency_nodes's list
        self.adjacency_nodes[src_name].append(dest_name)
        # Add in edgeweights
        self.edge_weights[(src_name, dest_name)] = weighted_edge.getWeight()

    # Return distans of between nodes
    def getEdgeWeight(self, edge: Edge):
        if (edge.src_name, edge.dest_name) in self.edge_weights:
            return self.edge_weights[(edge.src_name, edge.dest_name)]
        else:
            return None

    # Print
    # Print Nodes
    def printNodes(self):
        print("Node = ", end="")
        print(self.node_names)
        print()

    # Print Edge
    def printEdges(self):
        print("Edges : ", end="")
        enter_count = 0
        for weighted_edge in self.weighted_edges:
            if enter_count % 4 == 0:
                print()
            print(weighted_edge, end=",  ")
            enter_count += 1
        print("\n")

    # Print distance Table
    def printDistanceTable(self):
        print("Inter City Distance table :")
        print("    |", end="")
        for name in self.node_names:
            print("{:>4}".format(name), end="")
        print("\n-------------------------------------------------")
        for col_node in self.node_names:
            print("{:4}|".format(col_node), end="")
            for row_node in self.node_names:
                distance = self.getEdgeWeight(Edge(col_node, row_node))
                if col_node == row_node:
                    print("   0", end="")
                elif distance is None:
                    print("  oo", end="")
                else:
                    print("{:4}".format(distance), end="")
            print()
        print()


