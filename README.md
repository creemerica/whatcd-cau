# whatcd-cau
[![PyPI version](https://badge.fury.io/py/whatcd-cau.svg)](https://badge.fury.io/py/whatcd-cau)
[![PyPI license](https://img.shields.io/pypi/l/whatcd-cau.svg)](https://img.shields.io/pypi/l/whatcd-cau.svg)

Create and upload torrents to What.cd.

## Requirements
Creating torrents requires [mktorrent](http://mktorrent.sourceforge.net/)

## Installation

`$ pip install whatcd-cau`

## Usage

```python
from whatcd import Whatcd

what = Whatcd('username', 'password')
create = what.create('Sketch 2', 'Sketch_v2.torrent', '20')
upload = what.upload('Sketch v2', 'sketch, vector', 'Sketch version 2!', 'Sketch_v2.torrent')
```