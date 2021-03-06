import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now
# 1) we have a top level README file and
# 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name = "class5_edureka",
    version = "0.0.1",
    author = "Ganesh",
    author_email = "ganesh@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "example documentation tutorial",
    packages=['store', 'tests'],
    long_description="read('README')",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)