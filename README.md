asciinet
========

asciinet is a wrapper over the [ascii-graphs](https://github.com/cosminbasca/ascii-graphs) library for printing [networkx](https://networkx.github.io/) graphs as ASCII.

Important Notes
---------------
This software is the product of research carried out at the [University of Zurich](http://www.ifi.uzh.ch/ddis.html) and comes with no warranty whatsoever. Have fun!

TODO's
------
* The project is not documented (yet)

How to Install the Project
--------------------------
First make sure java is installed on your system. To install **asciinet** follow these instructions:

```sh
$ git clone https://github.com/cosminbasca/asciinet
$ cd asciinet/pyasciinet
$ python setup.py install
```

Also have a look at the build.sh script included in the codebase for a complete setup of the build process

Example
-------

```python
import networkx as nx
from asciinet import graph_to_ascii

#
# create a simple graph
#
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (3, 4), (1, 4), (2, 4)])

#
# should print
#  ┌───────┐
#  │   1   │
#  └┬────┬┬┘
#   │    ││
#   │    └┼───┐
#   v     v   │
# ┌───┐ ┌───┐ │
# │ 2 │ │ 3 │ │
# └──┬┘ └─┬─┘ │
#    │    │   │
#    │   ┌┼───┘
#    │   ││
#    v   vv
#  ┌───────┐
#  │   4   │
#  └───────┘
#
print graph_to_ascii(G)




```

Thanks a lot to
---------------
* [University of Zurich](http://www.ifi.uzh.ch/ddis.html) and the [Swiss National Science Foundation](http://www.snf.ch/en/Pages/default.aspx) for generously funding the research that led to this software.
