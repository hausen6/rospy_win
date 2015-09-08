#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
        name="rospy",
        author="hausen6",
        description="rospy for windows (indigo)",
        packages=find_packages("src"),
        package_dir={"": "src", }
        # install_requires = ["rospkg>=1.0.35",
        #                     "catkin_pkg>=0.2.10",
            # ]
)
