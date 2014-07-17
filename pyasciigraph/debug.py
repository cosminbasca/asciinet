import networkx as nx
from asciinet import graph_to_ascii

__author__ = 'basca'

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1, 2)
    G.add_edges_from([(1, 2), (1, 3)])

    print graph_to_ascii(G)