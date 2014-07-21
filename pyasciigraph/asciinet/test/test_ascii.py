from asciinet import graph_to_ascii
from asciinet.test.base import BaseTestCase


__author__ = 'basca'


class TestClient(BaseTestCase):
    def test_to_ascii(self):
        ascii = graph_to_ascii(self.graph)
        self.assertEqual(ascii.replace('\n', '').replace(' ', '').replace('\t', '').strip(), self.graph_repr)
