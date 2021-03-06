# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-29 17:41:58
@UpdateDate: 2019-10-24 21:10:35
@Description: 发布包的配置
    https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
'''

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name='xhpubs',
    version="0.0.1",
    author="lamborghini1993",
    author_email="1323242382@qq.com",
    description='a pub library for python',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/lamborghini1993/mypypi/tree/master/xhpubs',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
