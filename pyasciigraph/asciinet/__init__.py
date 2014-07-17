from collections import OrderedDict
from natsort import natsorted
import networkx as nx
import os

__author__ = 'basca'

__LIB__ = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
__JARS__ = natsorted([(jar.replace("asciigraph-assembly-", "").replace(".jar", ""),
                       os.path.join(__LIB__, jar))
                      for jar in os.listdir(__LIB__) if jar.startswith("asciigraph-assembly-")],
                     key=lambda (ver, jar_file): ver)
__JARS_DICT__ = OrderedDict()
for k, v in __JARS__:
    __JARS_DICT__[k] = v


def graph_to_ascii(graph):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')
    return ''
