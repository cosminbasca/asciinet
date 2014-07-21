# !/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

NAME = 'asciinet'

str_version = None
execfile('{0}/__version__.py'.format(NAME))

# Load up the description from README
with open('README') as f:
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