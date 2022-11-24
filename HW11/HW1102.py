# HW1102.py
# HW 11.2 Applications of MyGraph.py
"""
Project : Applications of MyGraph.py
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 24
Update list:
    - v1.1 : 11 / 24
        Import : MyGraph.py's Node, Edge, WeightedEdge, WeightedGraph
        Import : sys
        Make text file : KR_interCityDist.txt
        Make funtion : Dijkstra, initGraph, main
        
"""
from MyGraph import Node, Edge, WeightedEdge, WeightedGraph
import sys

PLUS_INF = sys.maxsize


# Use Sequential Search
def Dijkstra(G: WeightedGraph, start_name, end_name):
    if (start_name not in G.node_names) and (end_name not in G.node_names):
        raise ValueError("")

    weighted_nodes = {}  # to save node's shorter path & distance from start
    # init : weighted_nodes, weighted_nodes[start_node]
    for node in G.nodes:
        weighted_nodes[node.getName()] = {}
        weighted_nodes[node.getName()]["path"] = ""
        weighted_nodes[node.getName()]["distance"] = PLUS_INF
    weighted_nodes[start_name] = {}
    weighted_nodes[start_name]["distance"] = 0
    weighted_nodes[start_name]["path"] = start_name

    node_travel = []    # start node -> level 1 node -> level 2 node ...
    node_travel.append(start_name)
    now_node = start_name
    i = 1
    while i < len(weighted_nodes):  # check and data save adjacency node from low level
        ad_nodes = G.adjacency_nodes[now_node]
        for ad_node in ad_nodes:
            distance = G.getEdgeWeight(
                Edge(now_node, ad_node)) + weighted_nodes[now_node]["distance"]
            path = weighted_nodes[now_node]["path"]
            if distance is None:
                continue
            elif weighted_nodes[ad_node] is None:
                weighted_nodes[ad_node]["distance"] = distance
                weighted_nodes[ad_node]["path"] = path + " -> " + ad_node
            else:
                if weighted_nodes[ad_node]["distance"] > distance:
                    weighted_nodes[ad_node]["distance"] = distance
                    weighted_nodes[ad_node]["path"] = path + " -> " + ad_node
        if end_name in ad_nodes:
            yield weighted_nodes[end_name]["path"]
            yield weighted_nodes[end_name]["distance"]
            return
        for node in ad_nodes:
            if node not in node_travel:
                node_travel.append(node)
        now_node = node_travel[i]
        i += 1
    return None


def initGraph(file_name) -> WeightedGraph:
    G = WeightedGraph()
    name_set = set()
    with open(file_name, "r") as distance_data_lines:
        for distance_data in distance_data_lines:
            src_name, dest_name, distance = distance_data.split()
            name_set.add(src_name)
            name_set.add(dest_name)
            G.addNode(Node(src_name))
            G.addNode(Node(dest_name))
            G.addEdge(WeightedEdge(src_name, dest_name, int(distance)))
            G.addEdge(WeightedEdge(dest_name, src_name, int(distance)))
    print("initGraph() - adding nodes into Graph : ", end="")
    for name in name_set:
        print(name, end=", ")
    print()
    return G


if __name__ == "__main__":
    G = initGraph("KR_interCityDist.txt")
    G.printNodes()
    G.printEdges()
    G.printDistanceTable()

    start_name = "GJ"
    end_name = "SC"
    path, distance = Dijkstra(G, start_name, end_name)
    print("Found shortestPath_Dijkstra ({} -> {})".format(start_name, end_name))
    print("path = {}, distance = {}".format(path, distance))

    print()

    start_name = "SC"
    end_name = "GJ"
    path, distance = Dijkstra(G, start_name, end_name)
    print("Found shortestPath_Dijkstra ({} -> {})".format(start_name, end_name))
    print("path = {}, distance = {}".format(path, distance))
