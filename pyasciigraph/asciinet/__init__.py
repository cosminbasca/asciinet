from collections import OrderedDict
from subprocess import Popen, PIPE, call
from natsort import natsorted
import networkx as nx
import os

__author__ = 'basca'

__ASCII_CLASS__ = '.'.join(['com', 'ascii', 'AsciiGraph'])
__LIB__ = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
__JARS__ = natsorted([(jar.replace("asciigraph-assembly-", "").replace(".jar", ""),
                       os.path.join(__LIB__, jar))
                      for jar in os.listdir(__LIB__) if jar.startswith("asciigraph-assembly-")],
                     key=lambda (ver, jar_file): ver)
__JARS_DICT__ = OrderedDict()
for k, v in __JARS__:
    __JARS_DICT__[k] = v

__all__ = ['graph_to_ascii', 'JavaNotFoundException']


class JavaNotFoundException(Exception):
    pass


def graph_to_str(graph):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')
    return "{0}\n{1}\n".format(
        '\n'.join(['vertex: {0}'.format(v) for v in graph.nodes_iter()]),
        '\n'.join(['edge: {0}, {1}'.format(e[0], e[1]) for e in graph.edges_iter()])
    )


def graph_to_ascii(graph):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')

    if call(['java', '-version']) != 0:
        raise JavaNotFoundException('Java is not installed in the system path. Java is needed to run graph_to_ascii!')

    ascii_opts = []
    latest_version, jar_path = __JARS__[-1]
    command = ["java", "-classpath", jar_path] + [__ASCII_CLASS__] + ascii_opts
    proc = Popen(command, stdout=PIPE, stdin=PIPE)

    graph_repr = graph_to_str(graph)
    proc.stdin.write("{0}".format(graph_repr))
    proc.stdin.write("END\n")
    graph_ascii = proc.stdout.read()
    return graph_ascii


if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1, 2)
    G.add_edges_from([(1, 2), (1, 3)])

    print graph_to_ascii(G)