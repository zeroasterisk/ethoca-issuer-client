
from setuptools import setup, find_packages
from ethocaissuerclient.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='ethocaissuerclient',
    version=VERSION,
    description='An API client allowing an Issuer to use Ethoca',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Alan Blount',
    author_email='zeroasterisk@gmail.com',
    url='https://github.com/zeroasterisk/ethoca-issuer-client',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'ethocaissuerclient': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        ethocaissuerclient = ethocaissuerclient.main:main
    """,
)
