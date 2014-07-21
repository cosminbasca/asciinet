import pstats
import cProfile

__author__ = 'basca'

def getgraph():
    import networkx as nx
    from asciinet import graph_to_ascii
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3, 4])
    G.add_edges_from([(1, 2), (1, 3), (3, 4), (1, 4), (2, 4)])
    print graph_to_ascii(G, timeout=1)

if __name__ == '__main__':
    cProfile.runctx("getgraph()", globals(), locals(), 'asciinet.prof')
    s = pstats.Stats('asciinet.prof')
    s.strip_dirs().sort_stats("time").print_stats()