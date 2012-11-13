#!/usr/bin/env python
# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name="Power",
    version="1.0",
    description="",
    author="Ilya Kulakov",
    author_email="kulakov.ilya@gmail.com",
    url="https://github.com/Kentzo/power",
    platforms=["Mac OS X 10.6+", "Windows XP+"],
    packages=['power'],
    scripts=['tests.py']
)