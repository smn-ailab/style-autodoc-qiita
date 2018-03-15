import sys

from setuptools import find_packages, setup

sys.path.append('.')

setup(
    name="my_tools",
    version="1.0",
    description="my sample tools",
    author="tshimura",
    author_email="",
    url="https://github.com/smn-ailab/style-autodoc-qiita",
    include_package_data=True,
    install_requires=[
    ],
    test_suite='nose.collector',
    packages=['my_tools.' + pkg for pkg in find_packages('my_tools')],
)
