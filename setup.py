from setuptools import setup, find_packages

setup(
    name = "matplotlib-cern",
    version = "0.1.1",
    description = "A matplotlib template package for CERN plots",
    author = "Georgios Christou",
    packages = find_packages(),
    install_requires=[
        "matplotlib",
    ],
)