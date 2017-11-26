#!/usr/bin/env python
#
# author: Cosmin Basca
#
# Copyright 2010 University of Zurich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from subprocess import Popen, PIPE, call
import uuid
from natsort import natsorted
import networkx as nx
import threading
import atexit
import os
import requests
from msgpack import dumps, loads
from requests.exceptions import ConnectionError, Timeout
from asciinet._libutil import latest_jar, check_java

__author__ = 'basca'

DEVNULL = open(os.devnull, 'w')

__all__ = ['graph_to_ascii', 'JavaNotFoundException', 'GraphConversionError']


class GraphConversionError(Exception):
    pass


class _AsciiGraphProxy(object):
    @staticmethod
    def instance():
        if not hasattr(_AsciiGraphProxy, "_instance"):
            _AsciiGraphProxy._instance = _AsciiGraphProxy()
        return _AsciiGraphProxy._instance

    def __init__(self, port=0):
        check_java("Java is needed to run graph_to_ascii")
        self._prefix = '{0}='.format(uuid.uuid1())
        ascii_opts = ['--port', str(port), '--die_on_broken_pipe', '--port_notification_prefix', self._prefix]
        latest_version, jar_path = latest_jar()
        self._command = ["java", "-classpath", jar_path] + ['.'.join(['com', 'ascii', 'Server'])] + ascii_opts
        self._proc = None
        self._port = None
        self._url = None
        self._start()

    def _start(self):
        self._proc = Popen(self._command, stdout=PIPE, stdin=PIPE)
        try:
            line = ''
            while not line.startswith(self._prefix):
                line = self._proc.stdout.readline().decode(encoding='UTF-8')
            self._port = int(line.replace(self._prefix, '').strip())
        except Exception as e:
            self._proc.kill()
            raise e
        self._url = 'http://127.0.0.1:{0}/asciiGraph'.format(self._port)

    def _restart(self):
        self._proc.kill()
        self._start()

    def graph_to_ascii(self, graph, timeout=10):
        try:
            graph_repr = dumps({
                'vertices': [str(v) for v in graph.nodes()],
                'edges': [[str(e[0]), str(e[1])] for e in graph.edges()],
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

    return _asciigraph.graph_to_ascii(graph, timeout=timeout).decode(encoding='UTF-8')
