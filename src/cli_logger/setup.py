from setuptools import setup

NAME = 'cli_logger'

setup(
      name=NAME,
      version='0.1',
      description='A module to log program outputs.',
      url='https://github.com/TomMeHo/cli_logger',
      author='Thomas Meder',
      author_email='thomas@familie-meder.net',
      license='GPL-3.0',
      packages=[NAME],
      zip_safe=False,
      install_requires=[
            'click',
            'colorama',
            'datetime'
      ]
)