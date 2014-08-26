#!/bin/bash
clear
echo "prepare ascii-graph jar ... "
ROOT_DIR="././../"
JAR_DIR=${ROOT_DIR}"target/scala-2.11/"
LIB_DIR=${ROOT_DIR}"pyasciigraph/asciinet/lib/"

CWD=`pwd`
cd ${ROOT_DIR}
sbt +compile +assembly
cd ${CWD}
cp `ls -t ${JAR_DIR}asciigraph-assembly-*.jar | head -1` ${LIB_DIR}

echo "install dependencies ... "
pip install -r "./dependencies.txt"
echo "testing asciinet ..."
nosetests --rednose -v -s ./asciinet/test/
echo "building module egg distribution ... "
python setup.py bdist_egg
echo "building source distribution ... "
python setup.py sdist --formats=gztar
echo "building module wheels distribution ... "
python setup.py bdist_wheel

echo "all done!"