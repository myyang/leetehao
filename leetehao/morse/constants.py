# encoding: utf-8

"""
Some constants of morse

release |release|, version |version|

.. versionadded:: 1.0

    Initial

Contents
--------

Classes:

Functions:

Variables:

* :data:`MAP_NUMERIC`
* :data:`MAP_NUMERIC_SHORT`
* :data:`MAP_PUNCTUATION`
* :data:`MAP_SYMBOL`
* :data:`MAP_ALPHA`
* :data:`MAP_FORWARD`
* :data:`MAP_FORWARD_SHORT`
* :data:`MAP_INVERSE`
* :data:`MAP_INVERSE_SHORT`

Members
-------

"""

from itertools import chain

MAP_NUMERIC = {
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

MAP_NUMERIC_SHORT = {
    '1': '.-',
    '2': '..-',
    '3': '...-',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '-...',
    '8': '-..',
    '9': '-.',
    '0': '-',
}

MAP_PUNCTUATION = {
    '.': '.-.-.-',
    ':': '---...',
    ',': '--..--',
    ';': '-.-.-.',
    '?': '..--..',
    '=': '-...-',
    "'": '.----.',
    '"': '.-..-.',
    '/': '-..-.',
    '!': '-.-.--',
    '-': '-....-',
    '_': '..--.-',
    '(': '-.--.',
    ')': '-.--.-',
    '@': '.--.-.',
    '$': '...-..-',
    '&': '.-...',
    '+': '.-.-.',
}

MAP_SYMBOL = {
    'AAAAA': '.-.-.-.-.-',
    'AAA': '.-.-.-',
    'EEEEE': '．．．．．',
    'AR': '.-.-.',
    'AS': '.-...',
    'TTTTT': '-----',
    'IMI': '..--..',
    'SK': '...-.-',
    'BT': '-...-',
    'SOS': '...---...',
}

MAP_ALPHA = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

MAP_FORWARD = dict(chain(MAP_NUMERIC.items(), MAP_PUNCTUATION.items(), MAP_ALPHA.items()))
MAP_FORWARD_SHORT = dict(
    chain(MAP_NUMERIC_SHORT.items(), MAP_PUNCTUATION.items(), MAP_ALPHA.items())
)

MAP_INVERSE = dict((v, k) for (k, v) in MAP_FORWARD.items())
MAP_INVERSE_SHORT = dict((v, k) for (k, v) in MAP_FORWARD_SHORT.items())

SPLIT = " "
