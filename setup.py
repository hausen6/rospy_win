#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
        name="rospy",
        author="hausen6",
        discription="rospy for windows (indigo)",
        packages=find_packages(),
        install_requires = ["rospkg>=1.0.35",
                            "catkin_pkg>=0.2.10",
            ]
)
