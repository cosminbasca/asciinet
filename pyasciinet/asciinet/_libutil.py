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
import os
from subprocess import call
from natsort import natsorted

__author__ = 'basca'

__LIB__ = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
__JARS__ = natsorted([(jar.replace("asciigraph-assembly-", "").replace(".jar", ""),
                       os.path.join(__LIB__, jar))
                      for jar in os.listdir(__LIB__) if jar.startswith("asciigraph-assembly-")],
                     key=lambda x: x[0])


def latest_jar():
    global __JARS__
    return __JARS__[-1]


class JavaNotFoundException(Exception):
    pass

DEVNULL = open(os.devnull, 'w')

def check_java(message=""):
    if call(['java', '-version'], stderr=DEVNULL) != 0:
        raise JavaNotFoundException(
            'Java is not installed in the system path. {0}'.format(message))
