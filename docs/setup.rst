.. _setup-label:

======================
Setup and Requirements
======================

.. contents::
   :local:
   :depth: 2


Requirements
============

SimpleCellRes is a python3 package that relies on the following packages to be
installed.

- `matplotlib <https://matplotlib.org/>`_ (>3.3.4): for basic plotting.

- `numpy <https://numpy.org/>`_ (>1.21.0): for arrays and general functionality.

- `dataclasses <https://docs.python.org/3/library/dataclasses.html#module-dataclasses>`_ (>0.4) for cell classes.

These are listed in 'requirements.txt' in the base directory of the repository.

Installation
============

The code is hosted on `GitHub <https://github.com/Hitham2496/cell-resampler/>`_,
to use the module clone the repository with either:

.. code-block:: bash

   $ git clone git@github.com:Hitham2496/cell-resampler.git

Or, if you have not configured your GitHub account with a SSH key:

.. code-block:: bash

   $ git clone https://github.com/Hitham2496/cell-resampler.git

Navigate to the directory created and install the package with:

.. code-block:: bash

   $ python setup.py install --user

Or, to use your code in your local environment

.. code-block:: bash

   $ pip install --user -e .

This will enable you to use the module via importing as usual in your python scripts
and notebooks:

.. code-block:: python

   #!/usr/bin/env python3
   import SimpleCellRes

PyPI
====

I aim to publish the package on PyPI and will provide corresponding installation
instructions here when this has been completed.

Testing
=======

SimpleCellRes has been developed with robust testing as the guiding principle, the
unit tests are included in the GitHub repository.

You can test your installation with:

.. code-block:: bash

   $ python -m pytest
