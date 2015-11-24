from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whatcd-cau',
    version='0.1',
    description='Create and upload torrents to What.cd',
    long_description=long_description,
    url='https://github.com/creemerica/whatcd-cau.git',
    author='Spencer Cree',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['whatcd', 'upload', 'torrent', 'mktorrent'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "requests==2.7.0"
    ]
)