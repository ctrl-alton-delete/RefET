import codecs
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Single sourcing code from here:
#   https://packaging.python.org/guides/single-sourcing-package-version/
here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

version = find_version("refet", "__init__.py")

# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='refet',
    version=version,
    description='ASCE Standardized Reference Evapotranspiration Functions',
    long_description=long_description,
    license='Apache',
    author='Charles Morton',
    author_email='charles.g.morton@gmail.com',
    url='https://github.com/DRI-WSWUP/RefET',
    download_url='https://github.com/DRI-WSWUP/RefET/archive/v{}.tar.gz'.format(version),
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pandas', 'pytz'],
    packages=['refet'],
    keywords='RefET Evapotranspiration',
    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
)
