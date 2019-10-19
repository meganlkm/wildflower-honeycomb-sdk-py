import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()
REQUIREMENTS = []


with open(os.path.join(BASEDIR, 'requirements.pip')) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        REQUIREMENTS.append(line)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(BASEDIR))

test_dependencies = [
    'pytest==3.0.6',
    'pytest-cov==2.4.0',
    'pytest-mock==1.5.0',
    'pylint==1.6.5',
    'httpretty==0.8.14'
]

setup(
    name='wildflower-honeycomb-sdk',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='SDK for use with the Wildflower Honeycomb API',
    long_description='Provides uniform access to all aspects of the honeycomb API as well as a direct GraphQL interface for more complex queries.',
    url='https://github.com/Wildflowerschools/py-honeycomb-sdk',
    author='optimuspaul',
    author_email='paul.decoursey@wildflowerschools.org',
    install_requires= [
        'wf-gqlpycgen>=0.5.7',
        'requests>=2.21',
        'Jinja2>=2.10',
        'gql>=0.1.0',
        'PyYAML>=3.13',
        'click>=6.7',
        'boto3>=1.9.213'
    ]
    tests_require = test_dependencies,
    extra_require = {
        'test': test_dependencies
    }
    entry_points={
        'console_scripts': [
            'honeycomb=cli:cli',
        ],
    }
)
