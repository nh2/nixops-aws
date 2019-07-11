import sys
import subprocess

from distutils.core import setup, Command


setup(name='nixops-aws',
      version='@version@',
      description='NixOS cloud deployment tool, but for aws',
      url='https://github.com/TOBE/UPDATED',
      author='Eelco Dolstra',
      author_email='eelco.dolstra@logicblox.com',
      packages=['nixopsaws', 'nixopsaws.data', 'nixopsaws.resources', 'nixopsaws.backends'],
      entry_points={'nixops': ['aws = nixopsaws.plugin']},
      py_modules=['plugin']
)
