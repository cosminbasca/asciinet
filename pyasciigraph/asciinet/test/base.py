# coding=utf-8
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
        except Exception, e:
            print 'Have exception in [{0}]: {1}, \ntraceback = \n{2}'.format(func.__name__, e, traceback.format_exc())

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




