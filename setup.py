try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Robot Simulator',
    'author': 'Jesse Hon',
    'author_email': 'jesse@jessehon.com',
    'version': '0.1',
    'packages': ['robot_simulator'],
    'install_requires': [],
    'scripts': [],
    'name': 'robotsimulator'
}

setup(**config)
