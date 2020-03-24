"""setup.py

Package configuration and dependencies.

Will Badart <Badart_William@bah.com>
created: MAR 2020
"""

from setuptools import setup

with open('./README.md') as fs:
    long_description = fs.read()

setup(name='checkpoints',
      version='1.0.1',
      author='Will Badart',
      author_email='Badart_William@bah.com',
      description='Cache results of functions returning pandas DataFrames.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.boozallencsn.com/Badart-William/checkpoints',
      py_modules=['checkpoints'],

      install_requires=[
          'pandas',
      ],

      project_urls={
          'Bug Reports': 'https://github.boozallencsn.com/Badart-William/checkpoints/issues',
      },
     )
