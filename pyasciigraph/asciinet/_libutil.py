import os
from natsort import natsorted

__author__ = 'basca'

__LIB__ = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
__JARS__ = natsorted([(jar.replace("asciigraph-assembly-", "").replace(".jar", ""),
                       os.path.join(__LIB__, jar))
                      for jar in os.listdir(__LIB__) if jar.startswith("asciigraph-assembly-")],
                     key=lambda (ver, jar_file): ver)


def latest_jar():
    global __JARS__
    return __JARS__[-1]