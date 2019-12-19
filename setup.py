#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


setup(
    name="lasersdk-artiq",
    version="0.2",
    description="ARTIQ controller for TOPTICA Laser SDK",
    long_description=open("README.rst").read(),
    author="Robert Jördens",
    author_email="rj@quartiq.de",
    url="https://github.com/quartiq/lasersdk-artiq",
    download_url="https://github.com/quartiq/lasersdk-artiq",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "aqctl_laser = lasersdk_artiq.aqctl_laser:main",
        ],
    },
    test_suite="lasersdk_artiq.test",
    license="LGPLv3+",
)
