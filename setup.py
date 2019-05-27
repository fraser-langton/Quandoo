from setuptools import setup, find_packages
import os

INSTALL_REQUIRES = ['requests']

license='MIT'
if os.path.exists('LICENSE'):
    license = open('LICENSE').read()

long_description = """
    Unofficial Quandoo APIs allow Quandoo agents to retrieve and edit their merchant data
  """

setup(name='Quandoo',
      version='1.1.0',
      description='Quandoo API',
      long_description=long_description,
      author='Fraser Langton',
      author_email='fraserbasil@gmail.com',
      url='https://github.com/fraser-langton/Quandoo',
      download_url='https://github.com/fraser-langton/Quandoo',
      license=license,
      packages=find_packages(),
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        install_requires=INSTALL_REQUIRES
      )