# Panflute: Pythonic Pandoc Filters

[![Python version](https://img.shields.io/pypi/pyversions/panflute.svg)](https://pypi.python.org/pypi/panflute/)
[![PyPI version](https://img.shields.io/pypi/v/panflute.svg)](https://pypi.python.org/pypi/panflute/)
[![Development Status](https://img.shields.io/pypi/status/panflute.svg)](https://pypi.python.org/pypi/panflute/)
[![Build Status](https://travis-ci.org/sergiocorreia/panflute.svg?branch=master)](https://travis-ci.org/sergiocorreia/panflute)

[panflute](http://scorreia.com/software/panflute/) is a Python package that makes creating Pandoc filters fun.

For a detailed user guide, documentation, and installation instructions, see
<http://scorreia.com/software/panflute/>. If you want to contribute, head [here](/CONTRIBUTING.md).


## Install

To install panflute, open the command line and type:

```bash
pip install panflute
```

- Support Python 2.7, 3.3 or later, pypy, and pypy3.
- On windows, the command line (``cmd``) must be run as administrator.

## Uninstall

```bash
pip uninstall panflute
```

## Dev Install

After cloning the repo and opening the panflute folder:

`python setup.py install`
: installs the package locally

`python setup.py develop`
: installs locally with a symlink so changes are automatically updated

In addition, if you use python2, you need to pasteurize the code before running tests. In this directory, Run

```bash
# install pasteurize if you didn't have it yet
pip2 install -U future
pasteurize -wnj 4 .
```

## Contributing

Feel free to submit push requests. For consistency, code should comply with [pep8](https://pypi.python.org/pypi/pep8) (in particular, `pep8 . --ignore=E265,E501,E701,E731` only), and with the style guides by [@kennethreitz](http://docs.python-guide.org/en/latest/writing/style/) and [google](http://google.github.io/styleguide/pyguide.html). Read more [here](/CONTRIBUTING.md).

## License

BSD3 license (following  `pandocfilters` by @jgm).

