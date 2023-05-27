# setup.py
from distutils.command.build import build
from setuptools import setup

class custom_build(build):
    sub_commands = [
        ('build_grpc', None),
    ] + build.sub_commands

setup(cmdclass={'build': custom_build})
