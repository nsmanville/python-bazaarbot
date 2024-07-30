========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-bazaarbot/badge/?style=flat
    :target: https://readthedocs.org/projects/python-bazaarbot/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/nsmanville/python-bazaarbot/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/nsmanville/python-bazaarbot/actions

.. |codecov| image:: https://codecov.io/gh/nsmanville/python-bazaarbot/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/nsmanville/python-bazaarbot

.. |version| image:: https://img.shields.io/pypi/v/bazaarbot.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/bazaarbot

.. |wheel| image:: https://img.shields.io/pypi/wheel/bazaarbot.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/bazaarbot

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/bazaarbot.svg
    :alt: Supported versions
    :target: https://pypi.org/project/bazaarbot

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/bazaarbot.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/bazaarbot

.. |commits-since| image:: https://img.shields.io/github/commits-since/nsmanville/python-bazaarbot/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/nsmanville/python-bazaarbot/compare/v0.0.0...main



.. end-badges

A simple agent-based free market simulator engine.

* Free software: MIT license

Installation
============

::

    pip install bazaarbot

You can also install the in-development version with::

    pip install https://github.com/nsmanville/python-bazaarbot/archive/main.zip


Documentation
=============


https://python-bazaarbot.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
