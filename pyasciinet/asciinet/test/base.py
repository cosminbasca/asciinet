# coding=utf-8
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
import traceback
from unittest import TestCase
import functools
import networkx as nx

__author__ = 'basca'


def catch_exception(func):
    @functools.wraps
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print ('Have exception in [{0}]: {1}, \ntraceback = \n{2}'.format(func.__name__, e, traceback.format_exc()))

    return wrapper


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = nx.Graph()
        cls.graph.add_node(1)
        cls.graph.add_nodes_from([2, 3, 4])
        cls.graph.add_edges_from([(1, 2), (1, 3), (3, 4), (1, 4), (2, 4)])

        cls.graph_repr = """
  ┌───────┐
  │   1   │
  └┬────┬┬┘
   │    ││
   │    └┼───┐
   v     v   │
 ┌───┐ ┌───┐ │
 │ 2 │ │ 3 │ │
 └──┬┘ └─┬─┘ │
    │    │   │
    │   ┌┼───┘
    │   ││
    v   vv
  ┌───────┐
  │   4   │
  └───────┘   """.replace("\n", "").replace("\t", "").replace(" ", "").strip()

    @classmethod
    def tearDownClass(cls):
        pass




