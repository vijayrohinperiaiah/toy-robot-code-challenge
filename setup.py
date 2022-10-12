import os

from setuptools import setup
import distutils.cmd

from toyrobot.commands_controller import CommandsController
from toyrobot.toyrobot import ToyRobot

class LintCommand(distutils.cmd.Command):
    description = 'Initiate lint - auto-analyzer'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('pylint toyrobot/ tests/')


setup(
    name='Toy Robot',
    description='ToyRobot Code Challenge in Python',
    packages=['toyrobot'],
    test_suite='tests',
    cmdclass={
        'lint': LintCommand,
    }

)