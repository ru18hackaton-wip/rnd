from setuptools import setup
import os

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, 'projectname', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='projectname',
    version=version['__version__'],
    packages=['projectname'],
    install_requires=['py_trees'],
    entry_points={
        'console_scripts': [
            'run-robot=projectname:main',
        ],
    },
)
