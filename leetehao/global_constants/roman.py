# encoding: utf-8

"""
Constants for roman

release |release|, version |version|

.. versionadded:: 1.0

    Initial

Contents
--------

Classes:

Functions:

Variables:

Members
-------

"""


ROMAN_UNIT = ('I', 'V', 1, 'X')
ROMAN_TENS = ('X', 'L', 10, 'C')
ROMAN_HUND = ('C', 'D', 100, 'M')
ROMAN_THOU = 'M'

ROMAN_VALUE = {
    'M': 1000,
    'C': 100, 'D': 500,
    'X': 10, 'L': 50,
    'I': 1, 'V': 5,
}

ROMAN_CORRECTION = {
    'CM': -200, 'CD': -200,
    'XC': -20, 'XL': -20,
    'IV': -2, 'IX': -2,
}
