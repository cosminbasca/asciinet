from collections import OrderedDict
from subprocess import Popen, PIPE, call
from natsort import natsorted
import networkx as nx
import os
import yaml

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


class JavaNotFoundException(Exception):
    pass


def graph_to_yaml(graph):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')
    return yaml.dump("""vertices: [{0}]
edges: [{1}]""".format(
        [str(v) for v in graph.nodes_iter()],
        [[str(e[0]), str(e[1])] for e in graph.edges_iter()]
    ))


def graph_to_ascii(graph):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')

    if call(['java', '-version']) != 0:
        raise JavaNotFoundException('Java is not installed in the system path. Java is needed to run graph_to_ascii!')

    ascii_opts = []
    command = ["java"] + [__ASCII_CLASS__] + ascii_opts
    proc = Popen(command, stdout=PIPE, stdin=PIPE)

    proc.stdin.writelines(graph_to_yaml(graph))
    ascii = proc.stdout.readline()
    return ascii


if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1, 2)
    G.add_edges_from([(1, 2), (1, 3)])

    print graph_to_ascii(G)