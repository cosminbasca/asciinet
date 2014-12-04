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
