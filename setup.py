# setup.py
from distutils.cmd import Command
from distutils.command.build_py import build_py
import os
import pkg_resources
from setuptools import setup

# https://stackoverflow.com/questions/52994857/how-do-i-generate-python-grpc-code-from-within-a-setuptools-installer-setup-py
class GrpcTool(Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import grpc_tools.protoc

        proto_include = pkg_resources.resource_filename('grpc_tools', '_proto')

        # print(os.getcwd())
        grpc_tools.protoc.main([
            'grpc_tools.protoc',
            '-I{}'.format(proto_include),
            '--proto_path=protos/',
            '--python_out=./src',
            '--grpc_python_out=./src',
            'protos/helloworld.proto'
        ])

class BuildPyCommand(build_py):
    def run(self):
        self.run_command('grpc')
        super(BuildPyCommand, self).run()

setup(
    cmdclass={
        'grpc': GrpcTool,
        'build_py': BuildPyCommand
    },
    setup_requires=[
        'grpcio-tools'
    ]
)
