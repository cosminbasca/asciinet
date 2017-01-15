# !/usr/bin/env python
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
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

NAME = 'asciinet'

str_version = None
print('{0}/__version__.py'.format(NAME))
exec(open('{0}/__version__.py'.format(NAME)).read())
#execfile('{0}/__version__.py'.format(NAME))

# Load up the description from README
with open('README.md') as f:
    DESCRIPTION = f.read()

pip_deps = [
    'networkx>=1.9',
    'natsort>=3.2.0',
    'requests>=2.3.0',
    'msgpack-python>=0.4.2',
]

manual_deps = [
]

setup(
    name=NAME,
    version=str_version,
    author='Cosmin Basca',
    author_email='cosmin.basca@gmail.com; basca@ifi.uzh.ch',
    # url=None,
    description='A wrapper around the scala ascii-graphs library',
    long_description=DESCRIPTION,
    classifiers=[
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Java',
        'Programming Language :: Scala',
        'Topic :: Software Development'
    ],
    packages=[NAME, '{0}/test'.format(NAME)],
    package_data={
        NAME: ['lib/*.jar']
    },
    install_requires=manual_deps + pip_deps,
    entry_points={
        # 'console_scripts': ['asyncrpc = asyncrpc.cli:main']
    }
)
