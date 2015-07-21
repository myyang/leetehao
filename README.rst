===============================
leetehao
===============================

.. image:: https://img.shields.io/travis/myyang/leetehao.svg
        :target: https://travis-ci.org/myyang/leetehao

.. comment image:: https://img.shields.io/pypi/v/leetehao.svg
        :target: https://pypi.python.org/pypi/leetehao


''

* Free software: BSD license
.. comment * Documentation: https://leetehao.readthedocs.org.

Features
--------

* Convert/inverse leet code
* Convert/inverse morse code

Examples
--------

Morse

.. code-block:: python

    >>> from leetehao import morse
    >>> morse.encode('hello world')
    '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    >>> morse.encode('.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
    'HELLO WORLD'



Leet

.. code-block:: python

    >>> from leetehao import leet
    >>> leet.encode('hello world')
    '}{[-[_[_()  vv()[z[_|)'
    >>> leet.encode('}{[-[_[_()  vv()[z[_|)')
    'HELLO WORLD'
