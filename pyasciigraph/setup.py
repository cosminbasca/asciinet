__author__ = 'Cosmin Basca'
__email__ = 'basca@ifi.uzh.ch; cosmin.basca@gmail.com'

from setuptools import setup, find_packages

str_version = None
execfile('asciinet/__version__.py')

pip_deps = [
    'networkx>=1.9',
    'natsort>=3.2.0',
]

manual_deps = [
]

setup(
    name='asciinet',
    version=str_version,
    description='a wrapper around the scala ascii-graphs library',
    author='Cosmin Basca',
    author_email='basca@ifi.uzh.ch',
    packages = ["asciinet", "asciinet/test"],
    include_package_data = True,
    zip_safe = False,
    install_requires=manual_deps + pip_deps,
    scripts=[
        # 'scripts/?.py',
    ],
)