.. title::
   SimpleCellRes documentation

===================================================================================
SimpleCellRes: Simple Cell Resampling of Multi-Dimensional Regions
===================================================================================

.. image:: https://github.com/Hitham2496/SimpleCellRes/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/Hitham2496/SimpleCellRes/

Welcome to the documentation for SimpleCellRes, a proof-of-concept module created
as a simple implementation of the cell resampling procedure of
`(Andersen and Maier, 2021) https://link.springer.com/article/10.1140/epjc/s10052-022-10372-3`_ 
for efficient sampling of phase spaces in Monte Carlo integration.

This package allows the user to efficiently sample multiple-dimensional spaces
according to in-built or user-defined metrics. The module may be integrated into
a Monte Carlo event generator or for demonstration purposes (or let me know if
you find another use!)

The code is hosted on `GitHub <https://github.com/Hitham2496/cell-resampler/>`_
where issues may be raised. I hope to publish the package to PyPI in early 2023.

Authors
=======
This code has been contributed to by `Hitham Hassan <https://github.com/Hitham2496/>`_
and was developed alongside my postgraduate research at the
`IPPP <https://www.ippp.dur.ac.uk/>`_, Durham University.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   setup
   autoapi/index
