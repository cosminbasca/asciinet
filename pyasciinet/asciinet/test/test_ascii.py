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
from asciinet import graph_to_ascii
from asciinet.test.base import BaseTestCase


__author__ = 'basca'


class TestClient(BaseTestCase):
    def test_to_ascii(self):
        ascii = graph_to_ascii(self.graph)
        self.assertEqual(ascii.replace("\n", "").replace("\t", "").replace(" ", "").strip(), self.graph_repr)
