import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
      name='cli_logger',
      version='1.1.0',
      description='A module to pretty-print outputs for command-line programs.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/TomMeHo/cli_logger',
      author='Thomas Meder',
      author_email='tom@tommho.net',
      license='BSD',
      packages=setuptools.find_packages(),
      zip_safe=False,
      install_requires=[
            'click >= 7.1.2',
            'colorama >= 0.4.4',
            'datetime >= 4.3'
      ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging"
      ],
      python_requires='>=3.6'
)
