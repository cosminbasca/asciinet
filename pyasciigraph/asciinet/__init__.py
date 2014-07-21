from subprocess import Popen, PIPE, call
from natsort import natsorted
import networkx as nx
import threading
import atexit
import os

__author__ = 'basca'

__LIB__ = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
__JARS__ = natsorted([(jar.replace("asciigraph-assembly-", "").replace(".jar", ""),
                       os.path.join(__LIB__, jar))
                      for jar in os.listdir(__LIB__) if jar.startswith("asciigraph-assembly-")],
                     key=lambda (ver, jar_file): ver)

DEVNULL = open(os.devnull, 'w')

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


class _AsciiGraphProxy(object):
    @staticmethod
    def instance():
        if not hasattr(_AsciiGraphProxy, "_instance"):
            _AsciiGraphProxy._instance = _AsciiGraphProxy()
        return _AsciiGraphProxy._instance

    def __init__(self):
        if call(['java', '-version'], stderr=DEVNULL) != 0:
            raise JavaNotFoundException(
                'Java is not installed in the system path. Java is needed to run graph_to_ascii!')
        ascii_opts = []
        latest_version, jar_path = __JARS__[-1]
        self._command = ["java", "-classpath", jar_path] + ['.'.join(['com', 'ascii', 'AsciiGraph'])] + ascii_opts
        self._proc = Popen(self._command, stdout=PIPE, stdin=PIPE)

    def graph_to_ascii(self, graph, timeout=20):
        graph_repr = graph_to_str(graph)
        self._proc.stdin.write("{0}".format(graph_repr))
        self._proc.stdin.write("END\n")

        def restart():
            self._proc.kill()
            self._proc = Popen(self._command, stdout=PIPE, stdin=PIPE)

        tout = threading.Timer(timeout, restart)
        tout.start()
        graph_ascii = self._proc.stdout.read()
        tout.cancel()

        return graph_ascii

    def close(self):
        self._proc.stdin.write("QUIT\n")
        tout = threading.Timer(2, self._proc.kill)
        tout.start()
        exit_ok = self._proc.stdout.read()
        if exit_ok != 'EXIT_OK':
            self._proc.kill()
        tout.cancel()


_asciigraph = _AsciiGraphProxy.instance()


@atexit.register
def _cleanup():
    _asciigraph.close()


def graph_to_ascii(graph, timeout=20):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')

    return _asciigraph.graph_to_ascii(graph, timeout=timeout)
