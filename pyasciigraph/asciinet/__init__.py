from subprocess import Popen, PIPE, call
from natsort import natsorted
import networkx as nx
import threading
import atexit
import os
import requests
from msgpack import dumps, loads
from requests.exceptions import ConnectionError, Timeout

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


class GraphConversionError(Exception):
    pass


class _AsciiGraphProxy(object):
    @staticmethod
    def instance():
        if not hasattr(_AsciiGraphProxy, "_instance"):
            _AsciiGraphProxy._instance = _AsciiGraphProxy()
        return _AsciiGraphProxy._instance

    def __init__(self, port=0):
        if call(['java', '-version'], stderr=DEVNULL) != 0:
            raise JavaNotFoundException(
                'Java is not installed in the system path. Java is needed to run graph_to_ascii!')
        ascii_opts = [str(port), '--die_on_broken_pipe']
        latest_version, jar_path = __JARS__[-1]
        self._command = ["java", "-classpath", jar_path] + ['.'.join(['com', 'ascii', 'Server'])] + ascii_opts
        self._proc = None
        self._port = None
        self._url = None
        self._start()

    def _start(self):
        self._proc = Popen(self._command, stdout=PIPE, stdin=PIPE)
        try:
            self._port = int(self._proc.stdout.readline())
        except Exception, e:
            self._proc.kill()
            raise e
        self._url = 'http://127.0.0.1:{0}/asciiGraph'.format(self._port)

    def _restart(self):
        self._proc.kill()
        self._start()

    def graph_to_ascii(self, graph, timeout=10):
        try:
            graph_repr = dumps({
                'vertices': [str(v) for v in graph.nodes_iter()],
                'edges': [[str(e[0]), str(e[1])] for e in graph.edges_iter()],
            })

            response = requests.post(self._url, data=graph_repr, timeout=timeout)
            if response.status_code == 200:
                return loads(response.content)
            else:
                raise ValueError('internal error: \n{0}'.format(response.content))
        except (ConnectionError, Timeout):
            self._restart()
            raise GraphConversionError('could not convert graph {0} to ascii'.format(graph))


    def close(self):
        self._proc.kill()


_asciigraph = _AsciiGraphProxy.instance()


@atexit.register
def _cleanup():
    _asciigraph.close()


def graph_to_ascii(graph, timeout=10):
    if not isinstance(graph, nx.Graph):
        raise ValueError('graph must be a networkx.Graph')

    return _asciigraph.graph_to_ascii(graph, timeout=timeout)
