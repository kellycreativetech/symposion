import sys

from setuptools import setup, find_packages


setup(
    name = "symposion",
    version = "1.0a1.kct.dev13", # I know this breaks conventions, sorry.
    description = "collection of Pinax apps for conferences",
    url = "https://github.com/pinax/symposion",
    author = "Brian Rosner",
    author_email = "brosner@gmail.com",
    packages = find_packages(),
    zip_safe = False
)
