from setuptools import setup

NAME = 'cli_logger'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
      name=NAME,
      version='1.0',
      description='A module to pretty-print outputs for command-line programs.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/TomMeHo/cli_logger',
      author='Thomas Meder',
      author_email='tom@tommho.net',
      license='BSD',
      packages=[NAME],
      zip_safe=False,
      install_requires=[
            'click',
            'colorama',
            'datetime'
      ],
      python_requires='>=3.6'
)
