from time import time
import networkx as nx
from asciinet import graph_to_ascii

__author__ = 'basca'

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3, 4])
    # G.add_edges_from([(1, 2), (1, 3), (3, 4), (1, 4), (2, 4), (2, 3)])
    G.add_edges_from([(1, 2), (1, 3), (3, 4), (1, 4), (2, 4)])

    t0 = time()
    print graph_to_ascii(G)
    print 'took {0} seconds'.format(time() - t0)
    for i in xrange(100):
        t0 = time()
        print graph_to_ascii(G, timeout=1)
        print 'took {0} seconds'.format(time() - t0)