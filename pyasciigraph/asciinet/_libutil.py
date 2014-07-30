import os
from subprocess import call
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


class JavaNotFoundException(Exception):
    pass

DEVNULL = open(os.devnull, 'w')

def check_java(message=""):
    if call(['java', '-version'], stderr=DEVNULL) != 0:
        raise JavaNotFoundException(
            'Java is not installed in the system path. {0}'.format(message))